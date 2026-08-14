
## O que é este simulado

É um **treino** no mesmo formato da prova prática:

1. O código **está quebrado** de propósito.  
2. Você **corrige** os erros (passo a passo abaixo).  
3. Sobe o site e testa.  
4. Usa o **Thunder Client** e **salva prints**.

---
--

## PASSO 0 — Preparar o ambiente

Abra o terminal **na pasta do simulado** e rode **um comando de cada vez**:

```powershell
cd "PROVAS\SIMULADO"
pip install -r requirements.txt
python app.py
```

**O que vai acontecer agora:** o programa **ainda deve falhar** (está quebrado).  
Leia o erro vermelho no terminal — ele ajuda a achar o arquivo.

Quando terminar todas as correções, o comando `python app.py` sobe sem erro e você abre:

`http://127.0.0.1:5000`

Para parar o servidor: `Ctrl + C`.

---

# PARTE 1 — Arrumar o código (passo a passo)

Faça **uma correção por vez**. Depois de cada uma: **salve** (`Ctrl + S`).


## Passo 2— Subir e testar no navegador

```powershell
python app.py
```

1. Abra `http://127.0.0.1:5000`  
2. Deve aparecer o **RaspaTec**  
3. Escolha modo **palavra** (tecnologia) e clique em **Raspar notícias**  
4. Deve aparecer uma tabela (precisa de internet para `www.tecmundo.com.br`)

**Checklist:**  
- [ ] Site abriu  
- [ ] Botão raspou e mostrou links

---

# PARTE 2 — Thunder Client + prints

Agora prove que a API funciona.  
**Todos os prints** vão para a pasta `prints_thunder`.

---

## Passo T1 — Instalar o Thunder Client

1. No Cursor / VS Code, abra **Extensões**.  
2. Busque: `Thunder Client`.  
3. Clique em **Install**.  
4. Abra o Thunder Client.  

**Print obrigatório:**  
- Nome do arquivo: `01_thunder_instalado.png`  
- Mostre a tela do Thunder aberto.

**Checklist:**  
- [ ] Print `01_thunder_instalado.png` salvo

---

## Passo T2 — GET índice da API (sem body)

| Campo | Valor |
|-------|--------|
| Method | `GET` |
| URL | `http://127.0.0.1:5000/api` |
| Body | **vazio** |

1. Clique em **Send**.  
2. Status esperado: **200**.  
3. No JSON deve aparecer `"projeto": "RaspaTec"` e a fonte do TecMundo.

**Print obrigatório:** `02_get_api.png`  
(mostre URL, status 200 e parte do JSON)

**Checklist:**  
- [ ] Print `02_get_api.png`

---

## Passo T3 — GET notícias com palavra-chave tecnologia

| Campo | Valor |
|-------|--------|
| Method | `GET` |
| URL | `http://127.0.0.1:5000/api/noticias?modo=palavra` |
| Body | **vazio** |

1. Clique em **Send**.  
2. Status esperado: **200**.  
3. Procure `"total"` no JSON (idealmente **> 0** com internet).  
4. Procure `"palavras_chave"` contendo `tecnologia`.

**Print obrigatório:** `03_get_noticias_palavra.png`

**Checklist:**  
- [ ] Print `03_get_noticias_palavra.png`

---

## Passo T4 — GET histórico de coletas

| Campo | Valor |
|-------|--------|
| Method | `GET` |
| URL | `http://127.0.0.1:5000/api/historico/coletas` |
| Body | **vazio** |

1. Clique em **Send**.  
2. Status esperado: **200** (pode voltar lista vazia `[]` se ainda não sincronizou).

**Print obrigatório:** `04_get_historico.png`

**Checklist:**  
- [ ] Print `04_get_historico.png`

---

## Passo T5 — POST sincronizar (grava no SQLite)

| Campo | Valor |
|-------|--------|
| Method | `POST` |
| URL | `http://127.0.0.1:5000/api/noticias/sincronizar?modo=palavra` |
| Body | **vazio** |

## Passo T6 — POST manual (JSON)

| Campo | Valor |
|-------|--------|
| Method | `POST` |
| URL | `http://127.0.0.1:5000/api/noticias/manual` |
| Header | `Content-Type` = `application/json` |
| Body | tipo **JSON** |

Cole este JSON no body:

```json
{
  "titulo": "Simulado RaspaTec — tecnologia no Cotemig",
  "url": "https://www.tecmundo.com.br/exemplo-simulado.html",
  "secao": "manual"
}
```

1. Clique em **Send**.  
2. Status esperado: **201**.

**Print obrigatório:** `06_post_manual.png`

**Checklist:**  
- [ ] Print `06_post_manual.png`

---

## Passo T7 — Confirmar histórico depois do POST

Repita o GET:

`http://127.0.0.1:5000/api/historico/coletas`

Agora a lista **não** deve estar vazia.

**Print obrigatório:** `07_get_historico_depois.png`

**Checklist:**  
- [ ] Print `07_get_historico_depois.png`

---

