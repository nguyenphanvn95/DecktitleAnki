from aqt import mw
from aqt.gui_hooks import reviewer_did_show_question, state_did_change
import json
import os

def set_title_default():
    profile_name = mw.pm.name
    mw.setWindowTitle(f"{profile_name} - Anki")

def update_title_with_deck(card):
    try:
        config = mw.addonManager.getConfig(__name__)
        if not config.get("enable_title", True):
            return
        deck_id = card.did
        deck_name = mw.col.decks.name(deck_id)
        profile_name = mw.pm.name
        icon = config.get("icon", "")
        fmt = config.get("title_format", "{profile} - Anki - {deck}")
        title = fmt.format(profile=profile_name, deck=deck_name, icon=icon)
        mw.setWindowTitle(title)
    except Exception as e:
        print("Decktitle Error:", str(e))

def on_state_change(old, new):
    if new == "deckBrowser":
        set_title_default()

reviewer_did_show_question.append(update_title_with_deck)
state_did_change.append(on_state_change)
