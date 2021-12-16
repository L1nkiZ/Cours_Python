# Expressions bien parenthésées

## Vérification

Dans cette exercice, le mot expression désigne une chaîne de caractères ne contenant que des parenthèses ouvrantes et fermantes comme par exemple : ```"(()())"```, ```"(()()"``` et ```"(())("```.

Une expression est bien parenthésée si le nombre de parenthèses ouvrantes est égal au nombre de parenthèses fermantes, et si quelque soit la position dans l'expression, le nombre de parenthèses ouvrantes qui précèdent cette position est toujours supérieur ou égal au nombre de parenthèses fermantes qui précèdent. Par exemple :

- ```"(()())"``` est une expression bien parenthésée ;
- ```"(()()"``` est mal parenthésée car il y a 3 parenthèses ouvrantes et 2 parenthèses fermantes ;
- ```"(()))("``` est mal parenthésée car le cinquième caractère est la troisième parenthèse fermante, alors qu'il n'y a que deux parenthèses ouvrantes qui précèdent.

### Question

Si dans le parcours de gauche à droite d'une expression, on utilise un compteur que l'on incrémente de 1 à chaque fois qu'on rencontre une parenthèse ouvrante et qu'on décrémente de 1 à chaque fois qu'on rencontre une parenthèse fermante, indiquez à quelle condition sur les valeurs prises par ce compteur l'expression est bien parenthésée.

### Question

Ecrivez une fonction ```bien_parenthésée``` qui renvoie la valeur ```True``` si la chaîne passée en paramètre est bien parenthésée, et la valeur ```False``` dans le cas contraire.

## Factorisation

On suppose que l'on travaille avec des expressions bien parenthésées. On appelle factorisation d'une expression bien parenthésée un découpage de cette expression en expressions bien parenthésées consécutives, chacune de ces expressions étant appelée facteur. Voici quelques factorisations d'expressions bien parenthésées :

- ```"(()())"``` == ```"(()())"``` (un seul facteur)
- ```"()(()())"``` == ```"()" * "(()())"``` (deux facteurs)
- ```"(())()(()())"``` == ```"(())" * "()" * "(()())"``` (trois facteurs)

### Question

Écrire une fonction ```nbre_facteurs``` qui retourne le nombre de facteurs que possède une expression bien parenthésée passée en paramètre.

### Question

Écrire une fonction ```factorisation``` qui retourne une chaîne de caractères correspondant à la chaîne de caractères passées en paramètre mais en insérant le caractère ```'*'``` entre les facteur.

- ```factorisation("(()())")``` retourne ```"(()())"``` ;
- ```factorisation("()(()())")``` retourne ```"()*(()())"```;
- ```factorisation("(())()(()())")``` retourne ```"(())*()*(()())"``` ;
