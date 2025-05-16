import aiohttp
from bs4 import BeautifulSoup


async def get_page(serch: str) -> str:
    url = f'https://ru.wikipedia.org/wiki/{serch}'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return '❌ Статья не найдена. Проверь написание.'

                html = await response.text()
                soup = BeautifulSoup(html, 'lxml')
                div = soup.find('div', id='mw-content-text')
                first_p = div.find('p') if div else None

                if first_p and first_p.text.strip():
                    text = first_p.text.strip()
                    return text
                else:
                    return "🧐 Статья пустая или не содержит текста."
    except Exception as e:
        return f'⚠️ Произошла ошибка: {e}'




    #     import requests
    #     responce = requests.get(url)
    #     if responce.status_code != 200:
    #         return '❌ Статья не найдена. Проверь написание.'
    #
    #     soup = BeautifulSoup(responce.content, 'lxml')
    #     div = soup.find('div', id='mw-content-text')
    #     first_p = div.find('p')
    #
    #     if first_p and first_p.text.strip():
    #         text = first_p.text.strip()
    #         return text
    #     else:
    #         return "🧐 Статья пустая или не содержит текста."
    # except Exception as e:
    #     return f'⚠️ Произошла ошибка: {e}'
