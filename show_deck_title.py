from aqt import mw
from aqt.reviewer import Reviewer
from aqt.gui_hooks import reviewer_did_show_question

def update_title_with_deck(card):
    deck_id = card.did
    deck_name = mw.col.decks.name(deck_id)
    profile_name = mw.pm.name
    mw.form.setWindowTitle(f"{profile_name} - Anki - {deck_name}")

reviewer_did_show_question.append(update_title_with_deck)
