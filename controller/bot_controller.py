from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

calc_dict = {}


def get_info():
    company_info = {'about': '',
                    'contacts': '',
                    }
    # query = CompanyInfo.query.order_by(CompanyInfo.id.desc()).first()
    # if query:
    #     company_info = {'about': query.about,
    #                     'contacts': query.contact,
    #                     }

    return company_info