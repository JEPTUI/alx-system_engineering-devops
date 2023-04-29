#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
* infinite_while - create infinite loop
* Return: Always 0
*/
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/**
* main - create zombie processes
* Return: infinite while zombies
*/
int main(void)
{
	pid_t pid;
	unsigned int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", pid);
	}
	return (infinite_while());
}
