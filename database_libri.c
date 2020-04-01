#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define NomeFile "censimento_libri.txt"
#define N 20

struct book{
	unsigned int code;
	char title[250];
	char author[250];
	unsigned int year;
};


/* funzione per inserimento nuovi libri nel database */
void inserimento_libro(struct book* my_book){
	printf("Inserimento di un nuovo libro: \n");
	printf("Inserire il codice del libro: ");
	scanf("%d",&my_book->code);
	getchar();
	printf("Inserire il titolo del libro: ");
	gets(my_book->title);
	printf("Inserire l'autore: ");
	gets(my_book->author);
	printf("Inserire l'anno di pubblicazione: ");
	scanf("%d",&my_book->year);
	getchar();
	printf("\n");
}


/* funzione che controlla se il codice di un libro già apparare nella lista dei codici nel database */
int check_code(struct book* my_book,struct book lista_database[],int len){
	int i;
	for(i=0;i<len;i++)
		if(my_book->code == lista_database[i].code)
			return 1;
	return 0;
}


/* funzione che consente di trasferire a file le modifiche fatte al database */
void salvataggio_database(struct book lista_database[],int j, FILE* p_file){
	if (p_file = fopen(NomeFile,"w")){
		int i;
		for(i=0;i<j;i++){
			fprintf(p_file,"%d, %s, %s, %d\n",lista_database[i].code,lista_database[i].title,lista_database[i].author,lista_database[i].year);
		}
		fclose(p_file);
	}
}


/* funzione per la ricerca di un libro tramite titolo nel database */
int ricerca_titolo(struct book lista_database[],int j,char title[]){
	int i;
	for(i=0;i<j;i++)
		if (strcmp(lista_database[i].title,title) == 0)
			return i;
	return -1;
}

/* funzione per la cancellazione di libri presenti nel database (sia provvisorio che a file) */
int cancellazione_titolo(struct book lista_database[], int j, int codice){
	int i;
	for(i=0;i<j;i++){
		if(lista_database[i].code == codice){
			int k;
			for(k=i;k<j-1;k++)
				lista_database[k] = lista_database[k+1];
			return i;
		}
	} return -1;
}


/* funzione per il riordino del database per codice */
void insertion_sort_database(struct book lista_database[],int j){
	int i,k;
	struct book tmp;
	for(i=1;i<j;i++)
		for(k=i;k>=0;k--){
			if (lista_database[k].code < lista_database[k-1].code){
				tmp = lista_database[k];
				lista_database[k] = lista_database[k-1];
				lista_database[k-1] = tmp;
			} else break; 
		}
}

int main(void){
	FILE* p_file;
	struct book libro;
	char decisione;
	struct book lista_libri_nuovi[N];
	static struct book lista_database[200];
	int j=0;
	char row[520];
	if (p_file = fopen(NomeFile,"r")){
		while(fgets(row,sizeof(row),p_file)!= NULL){
			sscanf(row,"%d, %[^\n,], %[^\n,], %d",&libro.code,&libro.title,&libro.author,&libro.year);
			lista_database[j] = libro;
			j++;
		}
		fclose(p_file);
	} 
	else printf("Errore nell'aprertura del database.\n");
	printf("DATABASE LIBRI:\n\n\n");
	while(decisione!='q'){
		printf("Premi 1 per inserire un nuovo libro.\nPremi 2 per ricercare un libro tramite titolo.\nPremi 3 se intendi cancellare un libro.\nPremi 4 per ordinare il database per codice.\nPremi 5 per salvare le modifiche effettuate nel database.\nPremi q se vuoi uscire dal programma.\n\n");
		scanf("%c",&decisione);
		printf("\n");
		getchar();
		
		
		/* INSERIMENTO LIBRO */
		if (decisione == '1'){
			inserimento_libro(&libro);
			if (check_code(&libro,lista_database,j) == 0){
				lista_database[j] = libro;
				j++;
				printf("Libro inserito, per memorizzare nel database conferma tramite l'opzione 5 nel menu' principale.\n\n");
			} else {
			printf("ATTENZIONE: E' gia' presente in database un libro con lo stesso codice, non e' possibile memorizzare il libro specificato.\n\n");
			}
		}
		
		
		/* RICERCA PER TITOLO */
		else if (decisione == '2'){
			char ricerca[250];
			int idx;
			printf("Inserire il titolo da cercare nel database: ");
			scanf("%[^\n]",ricerca);
			getchar();
			idx = ricerca_titolo(lista_database,j,ricerca);
			if (idx == -1)
				printf("Titolo non trovato nel database.\n\n");
			else {
				printf("Titolo trovato:\nCodice: %d \nTitolo: %s \nAutore: %s \nAnno: %d \n\n",
						lista_database[idx].code,lista_database[idx].title,lista_database[idx].author,lista_database[idx].year);
			}
		}
		
		
		/* CANCELLAZIONE LIBRO */
		else if (decisione == '3'){
			int codice,idx;
			printf("Cancellazione libro: \n");
			printf("Inserire il codice del libro da cancellare nel database: ");
			scanf("%d",&codice);
			getchar();
			idx = cancellazione_titolo(lista_database,j,codice);
			if (idx == -1)
				printf("Libro non trovato, accertarsi che il codice sia corretto e riprovare.\n\n");
			else {
				j--;
				printf("Libro cancellato, per rendere la modifica permanente salvare dal menu' principale.\n\n");
			}	
		}
		
		
		/* RIORDINO PER CODICE */
		else if (decisione == '4'){
			insertion_sort_database(lista_database,j);
			printf("Riordino database per codice effettuato, per visualizzare la modifica salvare tramite menu' principale.\n\n");
		}
		
		
		
		/* SALVATAGGIO NUOVI LIBRI E CANCELLATI */
		else if (decisione == '5'){
			printf("Salvataggio nuovi inserimenti e cancellazioni..\n");
			salvataggio_database(lista_database,j,p_file);
			printf("Salvato con successo!\n\n");
		}
		
		
		/* CHIUSURA DEL PROGRAMMA */
		else if (decisione == 'q'){ 
			printf("Chiusura del programma...\n");
		}
	}
}
