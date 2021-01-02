from call_zmap import check_source
import hashlib
import db_settings
import os
import psycopg2
"""
source code for populating the database with csv file generated by zmap function code
"""
def return_ip_address_from_csv(csv_file_path):
    """return the list of all ip adress"""
    with open(csv_file_path, 'r') as file:
        file_lines = file.readlines()
        # remove newline special character
        ip_adress_list = [line.rstrip() for line in file_lines]
    return ip_adress_list
    

#openssl s_client -connect 54.172.100.205:443 -state | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > ./tmp/ssl_tmp.pem
#openssl x509 -text -in ./tmp/ssl_tmp.pem | sed -ne '/Subject Public Key Info/,/Exponent/p' > ./tmp/integer.txt
def get_certificate_info_from_ip_adress(ip_adress):
    """return dict with all info as values"""
    linux_opens_ssl_command = "openssl s_client -connect {}:443 -state | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > ./tmp/ssl_tmp.pem".format(ip_adress)
    os.system(linux_opens_ssl_command)
    os.system("openssl x509 -text -in ./tmp/ssl_tmp.pem | sed -ne '/Subject Public Key Info/,/Exponent/p' > ./tmp/integer.txt")
    with open('./tmp/integer.txt', "r") as tmp_file:
        info = tmp_file.readlines()
    encryption_algorithm = info[1].rstrip().replace(' ', '').split(':')[-1]
    hex_num = ''.join(info[4:-1]).strip().replace('\n', '').replace(' ', '').replace(':', '')
    # convert hex numb
    integer = int(hex_num, 16)
    #os.system("rm ./tmp/ssl_tmp.pem ./tmp/integer.txt")
    return integer, encryption_algorithm


def get_ip_adress_hash(ip_adress):
    #return ip adress hash
    return hashlib.md5(ip_adress.encode()).hexdigest()

def push_info_in_db(csv_file_path):
    ips = return_ip_address_from_csv(csv_file_path)
    if len(ips) == 0:
        raise('No IPs adress found')
    
    batch_information = dict()
    for ip in ips:
        # get numb and encryption algo 
        try:
            numb, algo = get_certificate_info_from_ip_adress(ip)
        except:
            continue
        ip_hash = get_ip_adress_hash(ip)
        batch_information[ip_hash] = dict()
        batch_information[ip_hash]['modulus'] = numb
        batch_information[ip_hash]['encryption_algo'] = algo 
        batch_information[ip_hash]['ip_adress'] = ip

    print(batch_information)
    #batch_information = {'1d9da03eb8d43cab07d53164d20f48f4': {'modulus': 25710902249855338163692580763482163515447647454052859507766027529004809431695093142478088829142461315650501674311563983344943807401764561695964736177408999295178311957884055836867310540001669933450100915923106261629139629492166659311710651608878959849100076520713969347682955503966029289158338976747506066375088078242024228756700161262382830342930700110428491569939040536203250552019135471840316583626292895743294654702902761789477182303155514084721515159181772785195876556440174317559324591358246911251083717216931497380528183568327887784779544964340145331697148388825565019982355018458065023578772221978347400053737, 'encryption_algo': 'rsaEncryption', 'ip_adress': '104.84.61.159'}, 'decb75677e1707f198a6a98af03fecb7': {'modulus': 30427733351130144490129528016127893666469496458576863123256486879794249613180162389526188147307904517349964095214665056162258041711333042123304234057037450420809991282433331330463090994542575753489319502976295094097238470981453911071925868012829701788600369523110261065834864995410275111267217024455688960786247804598196676395702060657482581080545399756595482380865524561163529755805242298067170484853753063890459018478254432957757775923198850297125611244264851036944028852506220682871440802785293103571373765235758822709854869871057488204747781286982984430602460801336048542539767600431601240943147634181985783410221, 'encryption_algo': 'rsaEncryption', 'ip_adress': '193.187.77.164'}}
    
    # connect to db 
    sql_where_clause_request = """SELECT * FROM ip_source WHERE ip_hash = %s;"""
    sql_insert_request = """
        INSERT INTO ip_source
        (
            ip_hash, 
            ip_adress, 
            encryption_algo,
            modulus
            ) 
        VALUES (%s, %s, %s, %s);
    """

    try:
        params = db_settings.DATABASES
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for ip_hash in batch_information:
            cur.execute(sql_where_clause_request, (ip_hash,))
            if cur.fetchall() != []:
                # we can now add a new header new
                print('this hash is already registered')
                continue
            
            modulus, encryption_algo, ip_adress = batch_information[ip_hash].values()
            modulus = str(modulus)
            cur.execute(sql_insert_request, (ip_adress, ip_adress, encryption_algo, modulus,))
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)



if __name__ == "__main__":
    path = "/Users/elhadjigagnysylla/Desktop/software/crypto/ssl-certificate-collision/data/results.csv"
    #ip_add = return_ip_address_from_csv(path)
    #ip_add = '68.168.193.126'
    #s, v = get_certificate_info_from_ip_adress(ip_add)
    #print(s)
    #print(v)
    #hash_ = get_ip_adress_hash(ip_add)
    #print(hash_)
    push_info_in_db(path)