import pytest
from server import app


@pytest.fixture(scope='module')
def test_client():
    flask_app = app
    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture
def json_result_content():
    JSON_RESULT_CONTENT = [
        {
            "text": "DARCY de 15/10/2018 a 21/10/2018",
            "path": ("/images/Cardapio/outubrorefeitorio2018"
                     "/DARCY-29-10-a-04-11.pdf"),
            "url": ("https://ru.unb.br/images/Cardapio/outubrorefeitorio2018"
                    "/CardapioDARCY-22a28-10.pdf")
        },
        {
            "text": "FCE, FGA e FUP de 15/10/2018 a 21/10/2018",
            "path": ("/images/Cardapio/outubrorefeitorio2018"
                     "/FUPFGAFCE29-10-a-04-11.pdf"),
            "url": ("https://ru.unb.br/images/Cardapio/outubrorefeitorio2018"
                    "/cardapioFGA-FCE-FUP-22a28-10.pdf")
        },
        {
            "text": "FAL de 15/10/2018 a 19/10/2018",
            "path": ("/images/Cardapio/outubrorefeitorio2018"
                     "/FAL29-10-a-04-11.pdf"),
            "url": ("https://ru.unb.br/images/Cardapio/outubrorefeitorio2018"
                    "/FAL29-10-a-04-11.pdf")
        }
    ]
    return JSON_RESULT_CONTENT


@pytest.fixture
def json_week_menu():
    JSON_WEEK_MENU = {
        "Monday": {
            "DESJEJUM": {
                "Bebidas quentes": "Leite e café",
                "Vegetariano": "Creme vegetal",
                "Achocolatado": "Achocolatado sem leite",
                "Pão": "Pão francês",
                "Complemento": "Carne moída",
                "Comp Vegetariano": "Patê funcional",
                "Fruta": "Melancia"
            },
            "ALMOÇO": {
                "Salada:": "Rúcula (somente FCE) Agrião e tomate",
                "Molho:": "Molho de laranja",
                "Prato Principal:": "Frango caramelizado",
                "Guarnição:": "Brócolis, milho e cenoura",
                "Prato Vegetariano:": "Soja em grão com couve flor",
                "Acompanhamentos:": "Arroz branco,\
                 Arroz integral e Feijão preto",
                "Sobremesa:": "Maçã",
                "Refresco:": "Limão"
            },
            "JANTAR": {
                "Salada:": "Alface lisa e picles",
                "Molho:": "Molho de manjericão",
                "Sopa:": "Creme de batata doce",
                "Pão:": "Torrada",
                "Prato Principal:": "Bife acebolado",
                "Prato Vegetariano:": "Curry de lentinha com leite de coco",
                "Acompanhamentos:": "Arroz branco,\
                 Arroz integral e Feijão preto",
                "Sobremesa:": "Laranja",
                "Refresco:": "Uva"
            }
        },
        "Tuesday": {
            "DESJEJUM": {
                "Bebidas quentes": "Café e leite",
                "Vegetariano": "Creme vegetal",
                "Achocolatado": "Achocolatado sem lactose",
                "Pão": "Pão careca / Bolo simples",
                "Complemento": "Queijo musarela",
                "Comp Vegetariano": "Vitamina de frutas",
                "Fruta": "Mamão"
            },
            "ALMOÇO": {
                "Salada:": "Alface crespa e beterraba ralada",
                "Molho:": "Molho argentino",
                "Prato Principal:": "Linguiça acebolada",
                "Guarnição:": "Purê de batata",
                "Prato Vegetariano:": "Quibe de legumes",
                "Acompanhamentos:": "Arroz branco, Arroz integral e Feijão",
                "Sobremesa:": "Banana",
                "Refresco:": "Manga"
            },
            "JANTAR": {
                "Salada:": "Couve e nabo com salsa",
                "Molho:": "Molho vinagrete",
                "Sopa:": "Sopa de fubá",
                "Pão:": "Torrada",
                "Prato Principal:": "Galinhada",
                "Prato Vegetariano:": "Hambúrguer ao molho pomodoro",
                "Acompanhamentos:": "Arroz com açafrão,\
                 Arroz integral e Feijão",
                "Sobremesa:": "Abacaxi",
                "Refresco:": "Acerola"
            }
        },
        "Wednesday": {
            "DESJEJUM": {
                "Bebidas quentes": "Café e leite",
                "Vegetariano": "Creme vegetal",
                "Achocolatado": "Achocolatado sem lactose",
                "Pão": "Pão francês",
                "Complemento": "Carne desfiada",
                "Comp Vegetariano": "Pasta de grão de bico",
                "Fruta": "Melão"
            },
            "ALMOÇO": {
                "Salada:": "Mix de folhas e rabanete",
                "Molho:": "Molho de limão",
                "Prato Principal:": "Bife ao molho de vinho",
                "Guarnição:": "Abóbora ao forno",
                "Prato Vegetariano:": "Nhoque a bolonhesa",
                "Acompanhamentos:": "Arroz branco, Arroz integral e Feijão",
                "Sobremesa:": "Mamão",
                "Refresco:": "Maracujá"
            },
            "JANTAR": {
                "Salada:": "Alface crespa e abobrinha com salsa",
                "Molho:": "Molho de soja com orégano",
                "Sopa:": "Sopa minestrone",
                "Pão:": "Torrada",
                "Prato Principal:": "Lasanha de espinafre com ricota",
                "Prato Vegetariano:": "Refogado de espinafre",
                "Acompanhamentos:": "Arroz branco, Arroz integral e Feijão",
                "Sobremesa:": "Maçã",
                "Refresco:": "Tangerina"
            }
        },
        "Thursday": {
            "DESJEJUM": {
                "Bebidas quentes": "Café e leite",
                "Vegetariano": "Creme vegetal",
                "Achocolatado": "Achocolatado sem lactose",
                "Pão": "Pão francês",
                "Complemento": "Ovos mexidos",
                "Comp Vegetariano": "Pasta de amendoim",
                "Fruta": "Trinca de fruta"
            },
            "ALMOÇO": {
                "Salada:": "Mostarda e tomate",
                "Molho:": "Molho de hortelã",
                "Prato Principal:": "Isca de frango ao shoyo",
                "Guarnição:": "Repolho refogado com tomate",
                "Prato Vegetariano:": "Ervilha com broto feijão e gergelim",
                "Acompanhamentos:": "Arroz colorido, Arroz integral e Feijão",
                "Sobremesa:": "Doce de banana",
                "Refresco:": "Guaraná"
            },
            "JANTAR": {
                "Salada:": "Agrião e cenoura ralada",
                "Molho:": "Molho verde",
                "Sopa:": "Creme de abóbora",
                "Pão:": "Torrada",
                "Prato Principal:": "Carré ao molho de alecrim",
                "Prato Vegetariano:": "Dahl de lentilha",
                "Acompanhamentos:": "Arroz branco, Arroz integral e Feijão",
                "Sobremesa:": "Melancia",
                "Refresco:": "Cajú"
            }
        },
        "Friday": {
            "DESJEJUM": {
                "Bebidas quentes": "Café e leite",
                "Vegetariano": "Creme vegetal",
                "Achocolatado": "Achocolatado sem lactose",
                "Pão": "Pão francês",
                "Complemento": "Mingau de aveia",
                "Comp Vegetariano": "Mingau de aveia de soja",
                "Fruta": "Abacaxi"
            },
            "ALMOÇO": {
                "Salada:": "Alface lisa e pepino",
                "Molho:": "Molho de erva picante",
                "Prato Principal:": "Feijoada",
                "Guarnição:": "Farofa  de couve",
                "Prato Vegetariano:": "Feijoada vegetariana",
                "Acompanhamentos:": "Arroz branco,\
                 Arroz integral e Feijão preto",
                "Sobremesa:": "Laranja",
                "Refresco:": "Limão"
            },
            "JANTAR": {
                "Salada:": "Alface lisa e maionese de batata",
                "Molho:": "Molho de salsa",
                "Sopa:": "Creme de legumes",
                "Pão:": "Torrada",
                "Prato Principal:": "Arroz con pollo",
                "Prato Vegetariano:": "Bolinho de grão de bico",
                "Acompanhamentos:": "Arroz branco,\
                 Arroz integral e Feijão preto",
                "Sobremesa:": "Banana",
                "Refresco:": "Maracujá"
            }
        }
    }
    return JSON_WEEK_MENU


@pytest.fixture
def corrupted_json():
    CORRUPTED_JSON = """
    [
        {
            "text": "DARCY de 15/10/2018 a 21/10/2018"
        },
        {
            "text": "FCE, FGA e FUP de 15/10/2018 a 21/10/2018"
        },
        {
            "text": "FAL de 15/10/2018 a 19/10/2018"
        },
        {
            text: wrong text
        }
    """
    return CORRUPTED_JSON


@pytest.fixture
def db_example():
    CORRECT_DOCUMENT = {
        "menu": {
            "Monday": {
                "DESJEJUM": {
                    "Bebidas quentes": "Leite e café",
                    "Vegetariano": "Creme vegetal",
                    "Achocolatado": "Achocolatado sem leite",
                    "Pão": "Pão francês",
                    "Complemento": "Carne moída",
                    "Comp Vegetariano": "Patê funcional",
                    "Fruta": "Melancia"
                },
                "ALMOÇO": {
                    "Salada:": "Rúcula (somente FCE) Agrião e tomate",
                    "Molho:": "Molho de laranja",
                    "Prato Principal:": "Frango caramelizado",
                    "Guarnição:": "Brócolis, milho e cenoura",
                    "Prato Vegetariano:": "Soja em grão com couve flor",
                    "Acompanhamentos:": "Arroz branco, \
                    Arroz integral e Feijão preto",
                    "Sobremesa:": "Maçã",
                    "Refresco:": "Limão"
                },
                "JANTAR": {
                    "Salada:": "Alface lisa e picles",
                    "Molho:": "Molho de manjericão",
                    "Sopa:": "Creme de batata doce",
                    "Pão:": "Torrada",
                    "Prato Principal:": "Bife acebolado",
                    "Prato Vegetariano:": "Curry de lentinha\
                     com leite de coco",
                    "Acompanhamentos:": "Arroz branco, \
                    Arroz integral e Feijão preto",
                    "Sobremesa:": "Laranja",
                    "Refresco:": "Uva"
                }
            },
            "Tuesday": {
                "DESJEJUM": {
                    "Bebidas quentes": "Café e leite",
                    "Vegetariano": "Creme vegetal",
                    "Achocolatado": "Achocolatado sem lactose",
                    "Pão": "Pão careca / Bolo simples",
                    "Complemento": "Queijo musarela",
                    "Comp Vegetariano": "Vitamina de frutas",
                    "Fruta": "Mamão"
                },
                "ALMOÇO": {
                    "Salada:": "Alface crespa e beterraba ralada",
                    "Molho:": "Molho argentino",
                    "Prato Principal:": "Linguiça acebolada",
                    "Guarnição:": "Purê de batata",
                    "Prato Vegetariano:": "Quibe de legumes",
                    "Acompanhamentos:": "Arroz branco, \
                    Arroz integral e Feijão",
                    "Sobremesa:": "Banana",
                    "Refresco:": "Manga"
                },
                "JANTAR": {
                    "Salada:": "Couve e nabo com salsa",
                    "Molho:": "Molho vinagrete",
                    "Sopa:": "Sopa de fubá",
                    "Pão:": "Torrada",
                    "Prato Principal:": "Galinhada",
                    "Prato Vegetariano:": "Hambúrguer ao molho pomodoro",
                    "Acompanhamentos:": "Arroz com açafrão, \
                    Arroz integral e Feijão",
                    "Sobremesa:": "Abacaxi",
                    "Refresco:": "Acerola"
                }
            },
            "Wednesday": {
                "DESJEJUM": {
                    "Bebidas quentes": "Café e leite",
                    "Vegetariano": "Creme vegetal",
                    "Achocolatado": "Achocolatado sem lactose",
                    "Pão": "Pão francês",
                    "Complemento": "Carne desfiada",
                    "Comp Vegetariano": "Pasta de grão de bico",
                    "Fruta": "Melão"
                },
                "ALMOÇO": {
                    "Salada:": "Mix de folhas e rabanete",
                    "Molho:": "Molho de limão",
                    "Prato Principal:": "Bife ao molho de vinho",
                    "Guarnição:": "Abóbora ao forno",
                    "Prato Vegetariano:": "Nhoque a bolonhesa",
                    "Acompanhamentos:": "Arroz branco, \
                    Arroz integral e Feijão",
                    "Sobremesa:": "Mamão",
                    "Refresco:": "Maracujá"
                },
                "JANTAR": {
                    "Salada:": "Alface crespa e abobrinha com salsa",
                    "Molho:": "Molho de soja com orégano",
                    "Sopa:": "Sopa minestrone",
                    "Pão:": "Torrada",
                    "Prato Principal:": "Lasanha de espinafre com ricota",
                    "Prato Vegetariano:": "Refogado de espinafre",
                    "Acompanhamentos:": "Arroz branco, \
                    Arroz integral e Feijão",
                    "Sobremesa:": "Maçã",
                    "Refresco:": "Tangerina"
                }
            },
            "Thursday": {
                "DESJEJUM": {
                    "Bebidas quentes": "Café e leite",
                    "Vegetariano": "Creme vegetal",
                    "Achocolatado": "Achocolatado sem lactose",
                    "Pão": "Pão francês",
                    "Complemento": "Ovos mexidos",
                    "Comp Vegetariano": "Pasta de amendoim",
                    "Fruta": "Trinca de fruta"
                },
                "ALMOÇO": {
                    "Salada:": "Mostarda e tomate",
                    "Molho:": "Molho de hortelã",
                    "Prato Principal:": "Isca de frango ao shoyo",
                    "Guarnição:": "Repolho refogado com tomate",
                    "Prato Vegetariano:": "Ervilha com broto \
                    feijão e gergelim",
                    "Acompanhamentos:": "Arroz colorido, \
                    Arroz integral e Feijão",
                    "Sobremesa:": "Doce de banana",
                    "Refresco:": "Guaraná"
                },
                "JANTAR": {
                    "Salada:": "Agrião e cenoura ralada",
                    "Molho:": "Molho verde",
                    "Sopa:": "Creme de abóbora",
                    "Pão:": "Torrada",
                    "Prato Principal:": "Carré ao molho de alecrim",
                    "Prato Vegetariano:": "Dahl de lentilha",
                    "Acompanhamentos:": "Arroz branco, \
                    Arroz integral e Feijão",
                    "Sobremesa:": "Melancia",
                    "Refresco:": "Cajú"
                }
            },
            "Friday": {
                "DESJEJUM": {
                    "Bebidas quentes": "Café e leite",
                    "Vegetariano": "Creme vegetal",
                    "Achocolatado": "Achocolatado sem lactose",
                    "Pão": "Pão francês",
                    "Complemento": "Mingau de aveia",
                    "Comp Vegetariano": "Mingau de aveia de soja",
                    "Fruta": "Abacaxi"
                },
                "ALMOÇO": {
                    "Salada:": "Alface lisa e pepino",
                    "Molho:": "Molho de erva picante",
                    "Prato Principal:": "Feijoada",
                    "Guarnição:": "Farofa  de couve",
                    "Prato Vegetariano:": "Feijoada vegetariana",
                    "Acompanhamentos:": "Arroz branco, \
                    Arroz integral e Feijão preto",
                    "Sobremesa:": "Laranja",
                    "Refresco:": "Limão"
                },
                "JANTAR": {
                    "Salada:": "Alface lisa e maionese de batata",
                    "Molho:": "Molho de salsa",
                    "Sopa:": "Creme de legumes",
                    "Pão:": "Torrada",
                    "Prato Principal:": "Arroz con pollo",
                    "Prato Vegetariano:": "Bolinho de grão de bico",
                    "Acompanhamentos:": "Arroz branco, \
                    Arroz integral e Feijão preto",
                    "Sobremesa:": "Banana",
                    "Refresco:": "Maracujá"
                }
            }
        },
        "dates": [
            "15/10/2018",
            "16/10/2018",
            "17/10/2018",
            "18/10/2018",
            "19/10/2018",
            "20/10/2018",
            "21/10/2018"
        ]
    }

    return CORRECT_DOCUMENT
