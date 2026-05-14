%A simple illustration of a Family Tree constising of One parent
%4 Children
%And 4 GrandChildren
%The First Part is always about the factual information
%Facts
parent(ngani, salome).
parent(ngani, roba).
parent(ngani, rose).
parent(ngani, kerina).
parent(salome, viki).
parent(roba, chief).
parent(rose, mike).
parent(kerina, mercy).

male(ngani).
male(roba).
male(chief).
male(mike).

female(salome).
female(rose).
female(kerina).
female(viki).
female(mercy).


%Rules
%A description of how the members relate to each other
grandparent(X, Z):- parent(X, Y) , parent(X, Y), parent(Y,Z).
aunt(X,Z):- parent(B,X), parent(B,Y), parent(Y,Z), female(X).
uncle(X,Z):- parent(B,X), parent(B,Y), parent(Y,Z), male(X).
niece(X,Z):- parent(A,Y), parent(A,Z), parent(Y,X),female(X).

