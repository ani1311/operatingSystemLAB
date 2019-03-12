#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE *createdFile,*openFile;
	char gotData[100],savedData[100] = "hello world\n";
	int i;

	createdFile = fopen("createdFile.txt","w");
	openFile = fopen("text.txt","r");

	fgets(gotData,100,openFile);
	
	i = 0;
	while(gotData[i] != '\0')
	{
		printf("%c",gotData[i]);
		i++;
	}


	fputs(savedData,createdFile);

	fclose(createdFile);
	fclose(openFile);
	

	return 0;
}
