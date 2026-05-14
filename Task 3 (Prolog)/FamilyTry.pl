parent(ngani, salome).
parent(salome, viki).
male(ngani).
female(salome).

grandparent(X,Z) :- parent(X,Y) ,parent(Y,Z).
