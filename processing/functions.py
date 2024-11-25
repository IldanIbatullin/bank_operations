from typing import List, Dict, Optional

def filter_by_state(transactions: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список транзакций по состоянию.

    :param transactions: Список словарей с данными о транзакциях.
    :param state: Статус транзакции для фильтрации.
    :return: Новый список словарей с отфильтрованными транзакциями.
    """
    return [transaction for transaction in transactions if transaction.get('state') == state]

