""" Bitmap Message, 
Affiche un message texte en fonction de l'image bitmap fournie."""

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
.................................................................... """

print('Bitmap Message')
print('Entrez le message à afficher avec le bitmap.')
message = input('> ')
if message == '':
  syd.exit()

# Boucle sur chaque ligne du bitmap
for line in bitmap.splitlines():
  # Boucle sur chaque caractère de la ligne :
  for i, bit in enumerate(line):
    if bit == ' ':
      # Imprimer un espace vide car il y a un espace dans le bitmap:
      print(' ', end='')
    else:
      # Afficher un caractère du message :
      print(message[i % len(message)], end='')
  print() # Afficher une nouvelle ligne.