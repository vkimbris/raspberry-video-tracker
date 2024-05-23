# Приложение для отправки кадров с камеры для детекции человека

## Установка

0. Выполните все шаги установки [этого](https://github.com/vkimbris/raspberry-motion-detector) приложения на виртуальная машине с IP <vm_host>
1. Убедитесь, что у вас установлен Python 3
2. Выполните команду `python3 -m pip install -r requirements.txt`
3. Выполнеите команду `python3 app/app.py --url http://<vm_host>:8000 --interval 1`
