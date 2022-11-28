import json

def load_candidates():
   """Загрузка json данных из файла"""
   with open('candidates.json','r',encoding="utf-8") as f:
      contents = json.load(f)

   return contents

def get_by_pk(pk):
   """функция возврата кандидата по номеру"""
   candidates = load_candidates()
   for candidate in candidates:
      if int(pk) == candidate['pk']:
         return candidate
      else:
         continue


def get_by_skill(skill_name):
   """Функция возврата кандидата по имени навыка"""
   candidates = load_candidates()
   candidate_list = []
   for candidate in candidates:
      if skill_name.lower() in candidate['skills'].lower():
         candidate_list.append(candidate)
      else:
         continue
   return candidate_list


