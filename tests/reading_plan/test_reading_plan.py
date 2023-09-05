from unittest.mock import Mock, patch
import pytest

from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)


@pytest.fixture
def db_mock():
    return [
        {
            "url": "https://blog.betrybe.com/carreira/oratoria/",
            "title": "Oratória: passo a passo para falar bem e se destacar!",
            "writer": "Lucas Custódio",
            "summary": "Sabemos que a arte de contar histórias surge ...",
            "reading_time": 15,
            "timestamp": "08/07/2022",
            "category": "Carreira",
        },
        {
            "url": "https://blog.betrybe.com/noticias/orkut-voltou/",
            "title": "Orkut voltou: o que se sabe até agora sobre o ...",
            "writer": "Allan Camilo",
            "summary": "Em meados de abril deste ano, o domínio ...",
            "reading_time": 4,
            "timestamp": "08/07/2022",
            "category": "Notícias",
        },
        {
            "url": "https://blog.betrybe.com/noticias/dungleon-como-jogar/",
            "title": "Dungleon: como jogar o game que mistura RPG e Wordle",
            "writer": "Allan Camilo",
            "summary": "Cópias e spin-offs de jogos populares  ...",
            "reading_time": 3,
            "timestamp": "07/07/2022",
            "category": "Notícias",
        },
        {
            "url": "https://blog.betrybe.com/carreira/livros-sobre-lideranca/",
            "title": "Os 20 livros sobre liderança para líderes de sucesso!",
            "writer": "Lucas Custódio",
            "summary": "Muitas pessoas desejam saber qual  ...",
            "reading_time": 1337,
            "timestamp": "04/07/2022",
            "category": "Carreira",
        },
    ]


def test_reading_plan_group_news(db_mock):
    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(-1)

    news_mock = Mock(return_value=db_mock)
    with patch("tech_news.analyzer.reading_plan.find_news", news_mock):
        result = ReadingPlanService.group_news_for_available_time(10)

    readable_groups = result["readable"]
    assert len(readable_groups) == 1

    first_readable_group = readable_groups[0]
    assert first_readable_group["unfilled_time"] == 3
    assert first_readable_group["chosen_news"] == [
        (
            "Orkut voltou: o que se sabe até agora sobre o ...",
            4,
        ),
        ("Dungleon: como jogar o game que mistura RPG e Wordle", 3),
    ]

    unreadable_news = result["unreadable"]
    assert unreadable_news == [
        ("Oratória: passo a passo para falar bem e se destacar!", 15),
        ("Os 20 livros sobre liderança para líderes de sucesso!", 1337),
    ]
