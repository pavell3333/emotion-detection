<div id="readme" class="Box-body readme blob js-code-block-container p-5 p-xl-6 gist-border-0">
    <article class="markdown-body entry-content container-lg" itemprop="text"><h1 dir="auto"><a id="user-content-задания-для-junior-data-scientist" class="anchor" aria-hidden="true" href="#задания-для-junior-data-scientist"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Задание.</h1>
<h2 dir="auto"><a id="user-content-1-разработать-веб-сервис-emotion-detection-с-помощью-multilabel-classification-на-базе-языковой-модели-bert" class="anchor" aria-hidden="true" href="#1-разработать-веб-сервис-emotion-detection-с-помощью-multilabel-classification-на-базе-языковой-модели-bert"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>1. Разработать Веб-сервис emotion-detection с помощью multilabel classification на базе языковой модели BERT.</h2>
<ul dir="auto">
<li>Для создания REST API можно использовать что удобно, FastApi, Flask, Django и т. п..</li>
<li>Модель и код запуска модели можно взять любую, готовую, например отсюда <a href="https://huggingface.co" rel="nofollow">https://huggingface.co</a> .</li>
<li>Достаточно одного REST эндпоинта POST /emotion-detection на вход которого подаётся текст, на выходе получаем набор вероятностей классов (радость, грусть, злость и т. п.).</li>
<li>Описать решение в README.md .</li>
<li>Код запушить в GitHub и предоставить ссылку.</li>
<li>Нужно будет объяснить, как работает сервис и выбранная модель.</li>
</ul>


</br>
<h3>Команды</h3>


<li>conda create --name emotion-detection</li>
<li>conda activate emotion-detection</li>
<li>pip install -r requirements.txt</li>
<li>uvicorn main:app --reload</li>


Была выбрана предобученная модель и токенайзер по ссылке:
</br>
https://huggingface.co/cointegrated/rubert-tiny2-cedr-emotion-detection

