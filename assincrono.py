import time
import urllib.request
import asyncio
import aiohttp

URL = 'https://api.github.com/events'
MAX_CLIENTS = 3

def fetch_sync(pid):
  print(f'Captura síncrona {pid} iniciou.')
  start = time.time()
  response = urllib.request.urlopen(URL)
  datetime = response.getheader('Date')

  print(f'Processo {pid}: {datetime}, demorou {(time.time() - start):.2f} segundos.')

  return datetime


@asyncio.coroutine
def fetch_async(pid):
  print(f'Captura assíncrona {pid} iniciou')
  start = time.time()
  response = yield from aiohttp.request('GET', URL)
  datetime = response.headers.get('Date')

  print(f'Processo {pid}: {datetime}, demorou: {(time.time() - start):.2f} segundos.')

  response.close()
  return datetime

def synchronous():
    start = time.time()
    for i in range(1, MAX_CLIENTS + 1):
        fetch_sync(i)
    print("Processo demorou: {:.2f} segundos".format(time.time() - start))


@asyncio.coroutine
def asynchronous():
    start = time.time()
    tasks = [asyncio.ensure_future(
        fetch_async(i)) for i in range(1, MAX_CLIENTS + 1)]
    yield from asyncio.wait(tasks)
    print("Processo demorou: {:.2f} segundos".format(time.time() - start))


print('Síncrono: ')
synchronous()

print('Assíncrono')
ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
ioloop.close()