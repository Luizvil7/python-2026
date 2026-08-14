# Service de webscraping — TecMundo (HTML + BeautifulSoup).
# Modelo: Aula 19 — requests → BeautifulSoup → lista estruturada.

from __future__ import annotations

import unicodedata
from typing import TypedDict
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

URL_FONTE: str = "https://www.tecmundo.com.br/"
TIMEOUT: int = 20
USER_AGENT: str = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0.0.0 Safari/537.36"
)

MODOS_VALIDOS: frozenset[str] = frozenset({"palavra", "todos"})

# Tema da prova: tecnologia (TecMundo quase não escreve a palavra nos <a>;
# por isso também aceitamos seções típicas de tech no path da URL).
PALAVRAS_CHAVE: tuple[str, ...] = ("tecnologia",)
SECOES_TECNOLOGIA: tuple[str, ...] = (
    "/software/",
    "/produto/",
    "/internet/",
    "/ciencia/",
    "/ciência/",
    "/seguranca/",
    "/segurança/",
    "/mobile/",
    "/voxel/",
)


class NoticiaItem(TypedDict):
    """Uma notícia / link extraído do HTML."""

    titulo: str
    url: str
    secao: str | None


class ResultadoBusca(TypedDict):
    """Pacote devolvido pelo scraping."""

    projeto: str
    fonte: str
    modo_busca: str
    palavras_chave: list[str]
    total: int
    noticias: list[NoticiaItem]


def _sem_acento(texto: str) -> str:
    """Remove acentos para comparação case/accent-insensitive."""
    nfkd = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def _secao_da_url(url: str) -> str | None:
    """Extrai o primeiro segmento do path."""
    path = urlparse(url).path
    partes = [p for p in path.split("/") if p]
    return partes[0] if partes else None


def _parece_candidato(url: str, titulo: str) -> bool:
    """Heurística: link do TecMundo com título longo o bastante."""
    if len(titulo.strip()) < 15:
        return False
    if not url.startswith("http"):
        return False
    host = urlparse(url).netloc.lower()
    if "tecmundo.com.br" not in host:
        return False
    bloqueados = (
        "/tag/",
        "/autor/",
        "/busca",
        "/login",
        "/assine",
        "/guia-de-compras",
        "javascript:",
        "awin1.com",
        "linksynergy",
    )
    return not any(b in url.lower() for b in bloqueados)


def _contem_palavra(titulo: str, url: str) -> bool:
    """True se título/URL tem 'tecnologia' ou se a URL é de seção de tech."""
    texto = _sem_acento(f"{titulo} {url}").lower()
    for p in PALAVRAS_CHAVE:
        if _sem_acento(p).lower() in texto:
            return True
    path = urlparse(url).path.lower()
    return any(s in path for s in SECOES_TECNOLOGIA)


def buscar_noticias(modo: str = "palavra") -> ResultadoBusca:
    """
    Função principal do scraping (tecnologia / TecMundo):
    1) baixa a página fonte
    2) percorre os <a href> com BeautifulSoup
    3) modo=palavra filtra por tecnologia / seções tech; modo=todos traz candidatos
    """
    modo_n = (modo or "palavra").strip().lower()
    if modo_n not in MODOS_VALIDOS:
        raise ValueError("Parâmetro modo deve ser 'palavra' ou 'todos'.")

    try:
        resposta = requests.get(
            URL_FONTE,
            timeout=TIMEOUT,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
                "Referer": URL_FONTE,
            },
        )
        resposta.raise_for_status()
    except requests.RequestException as erro:
        raise ConnectionError(f"Não foi possível acessar a fonte: {erro}") from erro

    resposta.encoding = resposta.apparent_encoding or "utf-8"
    soup = BeautifulSoup(resposta.text, "html.parser")

    vistos: set[tuple[str, str]] = set()
    noticias: list[NoticiaItem] = []

    for tag in soup.find_all("a", href=True):
        titulo = tag.get_text(" ", strip=True)
        url = urljoin(URL_FONTE, tag["href"]).split("#")[0].split("?")[0]
        if not _parece_candidato(url, titulo):
            continue

        if modo_n == "palavra" and not _contem_palavra(titulo, url):
            continue

        secao = _secao_da_url(url)
        chave = (titulo[:200], url)
        if chave in vistos:
            continue
        vistos.add(chave)

        noticias.append(
            NoticiaItem(
                titulo=titulo,
                url=url,
                secao=secao,
            )
        )

    return ResultadoBusca(
        projeto="RaspaTec",
        fonte=URL_FONTE,
        modo_busca=modo_n,
        palavras_chave=list(PALAVRAS_CHAVE),
        total=len(noticias),
        noticias=noticias,
    )
