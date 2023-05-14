from core.notifier import Notifier
import toml
from typing import List
import logging
from copy import deepcopy

def choose_drug_list_allergy(drug_list: List[str] = None, drug_list_additional: List[str] = None,
                          pollen_high = False):
    result_list = deepcopy(drug_list)
    if pollen_high:
        result_list.extend(drug_list_additional)
    print(result_list)
    return result_list


def make_notify_text(drug_list: List[str] = None, drug_list_additional: List[str] = None,
                          pollen_high = False):
    pollen_text = ''
    if pollen_high:
        pollen_text = 'ВЫСОКИЙ УРОВЕНЬ ПЫЛЬЦЫ\n\n'

    drugs = ", ".join(choose_drug_list_allergy(drug_list, drug_list_additional, pollen_high))
    print(drugs)
    return f'{pollen_text}Не забудь принять таблетки!\n{drugs}'


def main():
    pollen_status = True
    logging.basicConfig(filename=r'C:\\Users\nonam\PycharmProjects\aihelper\logging\human_log.log',
                        format='[%(levelname)s] %(asctime)s: %(message)s', datefmt='%Y-%m-%d',
                        level=logging.INFO, encoding='utf-8')

    with open(r'C:\\Users\nonam\PycharmProjects\aihelper\resources\drugs_list.toml', 'r', encoding='utf-8') as f:
        drug_data = toml.load(f)
        drug_list_important = drug_data['allergy']['drugs_important']
        drug_list_additional = drug_data['allergy']['drugs_additional']

    logging.info(f'Набор таблеток: '
                 f'{", ".join(choose_drug_list_allergy(drug_list_important, drug_list_additional, pollen_status))}')

    notify_text = make_notify_text(drug_list_important, drug_list_additional, pollen_status)
    notifier = Notifier()
    notifier.send_drugs_notify(notify_text)

    input()


if __name__ == '__main__':
    main()
