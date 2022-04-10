def countvocal(s):
    vocales=0
    word= set("aeiouAEIOU")
    for i in s:
        if i in word:
            vocales=vocales+1
    print("numero de vocales: ",vocales)      


s=str(input("ingresa palabra: "))
  
 
vowel_count=(s)

countvocal(s)
