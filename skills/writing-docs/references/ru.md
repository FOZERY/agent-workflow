# Russian artifacts

Read this file before you write or edit an artifact in Russian. It adapts the principles of [SKILL.md](../SKILL.md) to Russian. The rules of `SKILL.md` still apply. Where Russian grammar differs, this file wins.

## Words

- **Loan words.** Write a loan word that developers say aloud in Cyrillic: коммит, ветка, деплой, ревью. Keep a name in its original form: Codex, `main`, `pnpm test`, `AGENTS.md`.
- **Plain words.** Use the common Russian word, not the bureaucratic one: «это», not «является»; «этот», not «данный»; «сейчас», not «в данный момент»; «в задаче», not «в рамках задачи»; «позволяет», not «обеспечивает возможность».
- **Verbs, not verbal nouns.** «Удали ветку», not «осуществи удаление ветки». «Проверка выполняется» becomes «агент проверяет».
- **One term.** Pick one Russian word for one concept and keep it: if you wrote «воркер», do not switch to «исполнитель» or «агент-исполнитель».
- **No calques from English.** «Это логично», not «это делает смысл»; «решить проблему», not «адресовать проблему»; «в итоге», not «в конце дня».

## Sentences

- **Address.** Use one form of address in the whole artifact. If the project sets none, write instructions in the imperative with «ты»: «Запусти тесты».
- **Instructions.** One action per step, in the imperative. Do not write a step as an infinitive («Запустить тесты») or as a passive («Тесты запускаются»).
- **Length.** Keep the limits of `SKILL.md` as an upper bound: 20 words for a step, 25 for a description. A Russian sentence near the limit is usually too long. Split it.
- **Actor.** Name who acts: «оркестратор отправляет бриф», not «бриф отправляется». Use «-ся» passive only when the actor is unknown.
- **Participles.** Use at most one participial or adverbial participial phrase per sentence. Turn the rest into verbs or separate sentences.
- **Genitive chains.** Break a chain of three or more nouns in the genitive: «проверка соответствия требованиям безопасности» becomes «проверь, что код безопасен».
- **Small words.** Keep «уже», «ещё», «может», «поэтому», «но». They carry meaning.
- **«Только» and «не».** Put them next to the word that they change: «тесты запускаются только после ревью», not «только тесты запускаются после ревью» when you mean the time.
- **«Это» and «который».** Each must point to one obvious noun. If «это» points to a whole sentence, name the thing instead.
- **«И» and «или».** If both are in one sentence, show what each joins, or split the sentence.

## Punctuation

- **No long dash (—).** Use a verb, a comma or a new sentence: «`recap` пишет отчёт», not «`recap` — это скилл для отчёта». Keep the short dash in number ranges: 2–3.
- **Colon.** Use it only before a list, code or an example, or after a name in a list. Join an explanation with a word, or give it its own sentence.
- **No semicolons in prose, no slashes, no «(-и)».** Write two sentences, «и» or «или», and the plural.
- **Quotes.** Use «ёлочки» in prose. Keep code, commands and paths in backticks.

## Machine text to cut

These patterns make Russian text read as machine output. Delete them or replace them with the fact.

| Instead of | Write |
| --- | --- |
| Давайте разберёмся, как работает ревью. | Ревью запускает два субагента. |
| Важно отметить, что тесты нужно запускать после каждой правки. | Запускай тесты после каждой правки. |
| Скилл играет ключевую роль в обеспечении качества. | Скилл проверяет код по правилам проекта. |
| Это не просто проверка, а полноценный анализ. | Скилл проверяет стандарты и соответствие задаче. |
| Быстро, надёжно и удобно. | Сборка идёт 1 секунду. |
| Таким образом, мы получаем стабильный процесс. | (Delete. Stop after the last fact.) |
| Данный скилл позволяет осуществлять упрощение кода. | Скилл упрощает код. |
| В рамках задачи была выполнена проверка. | Агент проверил код. |

## Examples

| Instead of | Write | What changed |
| --- | --- | --- |
| Необходимо запустить тестовую команду. | Запусти `pnpm test`. | Imperative and the real command. |
| После проверки конфигурации перезапусти сервис и проверь ответ. | 1. Проверь конфигурацию.<br>2. Перезапусти сервис.<br>3. Проверь ответ. | Three actions become three steps. |
| Удали бэкап, если проверка восстановления прошла. | Если проверка восстановления прошла, удали бэкап. | The condition comes first. |
| Воркер только запускает тесты после ревью. | Воркер запускает тесты только после ревью. | «Только» limits the time. |
| Оркестратор отправляет бриф воркеру. Это может не сработать. | Оркестратор отправляет бриф воркеру. Отправка может не сработать. | The subject names the thing that fails. |
| Закоммить/запушь файл(ы). | Закоммить файлы. Пушь только с разрешения. | Two actions, two sentences, the plural. |
| Обработка ошибок валидации конфигурации осуществляется сервисом. | Если конфигурация неверна, сервис показывает ошибку. | Condition and verb replace the noun chain. |
| Миграция была выполнена на `abc123`, хотя проверка числа строк не проводилась. | Миграция прошла на `abc123`. Число строк не проверяли. | Event and gap get separate sentences. |

## Reread

After the checks of `SKILL.md`:

1. Is there a verbal noun or a bureaucratic word where a verb fits?
2. Is there a long dash anywhere outside code?
3. Does each step use the same form of address and the imperative?
4. Would a Russian-speaking developer say this word aloud?
