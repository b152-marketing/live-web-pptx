#!/bin/zsh
# Копирует манифест в папку надстроек PowerPoint для Mac.
set -e
cd "$(dirname "$0")"
WEF="$HOME/Library/Containers/com.microsoft.Powerpoint/Data/Documents/wef"
mkdir -p "$WEF"
cp manifest.xml "$WEF/live-web.manifest.xml"
echo "Готово. Перезапустите PowerPoint: Вставка → Надстройки → Мои надстройки → Developer Add-ins → Live Web"
