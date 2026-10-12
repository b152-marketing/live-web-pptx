# Live Web — iframe на слайде PowerPoint (macOS, Apple Silicon)

Office Content Add-in: объект на слайде, внутри которого живая веб-страница.
Работает в режиме редактирования и в показе слайдов. URL и интервал автообновления
сохраняются в самом файле .pptx (отдельно для каждого экземпляра на слайде).

Страница надстройки хостится на GitHub Pages: https://b152-marketing.github.io/live-web-pptx/

## Установка

```sh
./install.sh
```

Или вручную: скопируйте `manifest.xml` в
`~/Library/Containers/com.microsoft.Powerpoint/Data/Documents/wef/`.

Перезапустите PowerPoint → **Вставка → Надстройки → Мои надстройки → Developer Add-ins → Live Web**.
На слайде появится объект; наведите курсор и нажмите ⚙, чтобы задать URL.

## Ограничения

- Сайты с `X-Frame-Options` / CSP `frame-ancestors` не встраиваются (пустой кадр) — ограничение браузерного движка.
- Встраиваемая страница должна быть по https.
- Нужен интернет (надстройка и `office.js` грузятся по сети).
