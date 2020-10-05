#include <stdio.h>
int counter;
void tower(int disc,char *src,char *dest,char *aux);
int main()
{
	int noofdisc;
	printf("Enter number of disc in tower: ");
	scanf("%d",&noofdisc);
	tower(noofdisc,"Source","Destination","Auxilary");
	printf("\n\nTotal moves done: %d\n",counter);
}
void tower(int disc,char *src,char *dest,char *aux)
{
	if (disc>0)
	{
		tower(disc-1,src,aux,dest);
		printf("\nMove disc %d from %s to %s", disc,src,dest);
		counter++;
		tower(disc-1,aux,dest,src);
	}
}