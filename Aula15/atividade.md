PS C:\Users\22502556> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>   -Method POST `
>>   -ContentType "application/json" `
>>   -Body '{"titulo":"Cafe com Deus Pai Volume 1","autor":"Junior Rostirola","ano": 2022}'


ano          : 2022
autor        : Junior Rostirola
data_criacao : 2026-07-30 08:38:58.531057
id           : 4
titulo       : Cafe com Deus Pai Volume 1



PS C:\Users\22502556> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>   -Method POST `
>>   -ContentType "application/json" `
>>   -Body '{"titulo":"Cafe com Deus Pai Volume 2","autor":"Junior Rostirola","ano": 2021}'


ano          : 2021
autor        : Junior Rostirola
data_criacao : 2026-07-30 08:39:11.722956
id           : 5
titulo       : Cafe com Deus Pai Volume 2



PS C:\Users\22502556> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>   -Method POST `
>>   -ContentType "application/json" `
>>   -Body '{"titulo":"Cafe com Deus Pai Volume 3","autor":"Junior Rostirola","ano": 2025}'


ano          : 2025
autor        : Junior Rostirola
data_criacao : 2026-07-30 08:39:22.297046
id           : 6
titulo       : Cafe com Deus Pai Volume 3



PS C:\Users\22502556> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>   -Method POST `
>>   -ContentType "application/json" `
>>   -Body '{"titulo":"Cafe com Deus Pai Volume 4","autor":"Junior Rostirola","ano": 2025}'


ano          : 2025
autor        : Junior Rostirola
data_criacao : 2026-07-30 08:39:30.241124
id           : 7
titulo       : Cafe com Deus Pai Volume 4



PS C:\Users\22502556> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>   -Method POST `
>>   -ContentType "application/json" `
>>   -Body '{"titulo":"Cafe com Deus Pai Volume 6","autor":"Junior Rostirola","ano": 2026}'


ano          : 2026
autor        : Junior Rostirola
data_criacao : 2026-07-30 08:39:55.702961
id           : 8
titulo       : Cafe com Deus Pai Volume 6



PS C:\Users\22502556> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>   -Method POST `
>>   -ContentType "application/json" `
>>   -Body '{"titulo":"Cafe com Deus Pai Volume 7","autor":"Junior Rostirola","ano": 2026}'


ano          : 2026
autor        : Junior Rostirola
data_criacao : 2026-07-30 08:39:59.945469
id           : 9
titulo       : Cafe com Deus Pai Volume 7



PS C:\Users\22502556> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>   -Method POST `
>>   -ContentType "application/json" `
>>   -Body '{"titulo":"Cafe com Deus Pai Volume 8","autor":"Junior Rostirola","ano": 2027}'


ano          : 2027
autor        : Junior Rostirola
data_criacao : 2026-07-30 08:40:04.373680
id           : 10
titulo       : Cafe com Deus Pai Volume 8



PS C:\Users\22502556> Invoke-RestMethod http://127.0.0.1:5000/api/livros/4 `
>>    -Method PUT `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"O Senhor dos Aneis","autor":"J. R. R. Tolkien","ano": 1954}'


ano          : 1954
autor        : J. R. R. Tolkien
data_criacao : 2026-07-30 08:38:58.531057
id           : 4
titulo       : O Senhor dos Aneis



PS C:\Users\22502556> Invoke-RestMethod http://127.0.0.1:5000/api/livros/5 -Method DELETE

PS C:\Users\22502556> Invoke-RestMethod http://127.0.0.1:5000/api/livros/6 -Method DELETE

PS C:\Users\22502556> Invoke-RestMethod http://127.0.0.1:5000/api/livros/7 -Method DELETE



Resultado final do DB

ano          : 1949
autor        : George Orwell
data_criacao : 2026-07-30 08:37:51.854744
id           : 3
titulo       : 1984

ano          : 2026
autor        : Junior Rostirola
data_criacao : 2026-07-30 08:39:55.702961
id           : 8
titulo       : Cafe com Deus Pai Volume 6

ano          : 2026
autor        : Junior Rostirola
data_criacao : 2026-07-30 08:39:59.945469
id           : 9
titulo       : Cafe com Deus Pai Volume 7

ano          : 2027
autor        : Junior Rostirola
data_criacao : 2026-07-30 08:40:04.373680
id           : 10
titulo       : Cafe com Deus Pai Volume 8

ano          : 1899
autor        : Machado de Assis
data_criacao : 2026-07-30 08:37:51.854744
id           : 1
titulo       : Dom Casmurro

ano          : 1890
autor        : Aluísio Azevedo
data_criacao : 2026-07-30 08:37:51.854744
id           : 2
titulo       : O Cortiço

ano          : 1954
autor        : J. R. R. Tolkien
data_criacao : 2026-07-30 08:38:58.531057
id           : 4
titulo       : O Senhor dos Aneis
