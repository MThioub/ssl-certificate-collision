/*L'algorithme prend en entrée deux modules de RSA,
et calcule leur pgcd*/

#include <stdio.h>
#include <gmp.h>

int compare(mpz_t resultat,  mpz_t n1, mpz_t n2);

int main(int argc,char* argv[]){
  /*déclaration des variables*/

  mpz_t resultat, n1, n2;
  mpz_init(resultat);
  mpz_init(n1);
  mpz_init(n2);
  mpz_t x;
  mpz_init(x);
  mpz_set_ui(x,1);
  mpz_init(resultat);
  mpz_set_str(n1, argv[1], 10);
  mpz_set_str(n2, argv[2], 10);

  //printf ("\n Entrer le premier module RSA:\n");
  //gmp_scanf("%Zd", &n1);
  //printf ("\n Entrer le deuxième module RSA:\n");



  compare(resultat, n1, n2);
  //printf("%d", mpz_cmp(resultat,x));
  return mpz_cmp(resultat,x);
}




int compare(mpz_t resultat,  mpz_t n1, mpz_t n2) {


mpz_gcd(resultat, n1, n2);
return 0;

}
