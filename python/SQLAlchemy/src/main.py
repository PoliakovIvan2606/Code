import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from queries.orm import SyncOrm
from queries.core import SynCore

# # Создание таблиц
# SyncOrm.create_tebles()

# # Добавление данных
# SyncOrm.insert_workers()

# # Получение данных
# SyncOrm.select_workers()clear

# SynCore.create_tebles()
# SynCore.insert_workers()
# SynCore.update_workers()
# SynCore.select_workers()

# SyncOrm.insert_resumes()

SyncOrm.select_resumes_avg_compensation()