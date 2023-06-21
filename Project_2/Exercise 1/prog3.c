#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void denied(){
	puts("Access Denied.\n");
}
void granted(){
	puts("Access Granted.\n");
}
void smashed(){
	puts("Access granted. Gonna cry?\nYou should have thought of that earlier.\n");
	exit(1);
}
int check_authentication(char *password) {
	int auth_flag = 0;
	char password_buffer[16];
	strcpy(password_buffer, password);
	if(strcmp(password_buffer, "Parker") == 0)
		auth_flag = 1;
	if(strcmp(password_buffer, "Peter") == 0)
		auth_flag = 1;
	return auth_flag;
}
int main(int argc, char *argv[]) {
	if(argc < 2) {
		printf("Usage: %s <password>\n", argv[0]);
		exit(0);
	}
	if(check_authentication(argv[1])) 
		granted();
	else
		denied();
}
