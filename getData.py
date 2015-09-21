import pyodbc
 
def getAuthorStemmedPaper(authorID,excludePaperID):
    connAuth = pyodbc.connect(DRIVER='{SQL Server};SERVER=JUSTBE;UID=sa;PWD=1;DATABASE=additional_paper_coAuthors')
    stAuth = connAuth.cursor()
    stAuth.execute('EXEC GetAuthorsStemmedPaper @AuthorID =?, @ExcludePaperID = ?',(authorID,excludePaperID))
    for resultAuth in stAuth:
        return resultAuth[0] #.decode('utf-8', 'ignore')
    
    connAuth.close()


def getStemmedPaper(paperID):
    connPap = pyodbc.connect(DRIVER='{SQL Server};SERVER=JUSTBE;UID=sa;PWD=1;DATABASE=additional_paper_coAuthors')
    stPap = connPap.cursor()
    stPap.execute('EXEC GetNewStemmedPaper @PaperID =?',(paperID))
    for resultPap in stPap:
        #print str(len(resultPap[0])) + " -aaa"
        return resultPap[0].encode('ascii', 'ignore')
    stPap.close()