init python:

    character_say_state = {
        "active": False,
        "speaking": False
    }

    def manage_speaking_factory(character_object, speaking, nonspeaking):
        def manage_speaking(st, at):
            if character_say_state["speaking"] == character_object:
                return speaking, 1
            else:
                return nonspeaking, 1
        return manage_speaking

    def character_factory(name, kind=None, callback=None, *args, **kwargs):
        """
        Returns a tuple containing a character for use in ADV, followed
        by a tuple for use in NVL, given typical parameters to define
        a character using `Character`.

        Presently we assume that all arguments passed for the character
        to be used in ADV are the same for NVL. Here are the changes
        to the way the parameters are handled:
            1. `kind` is ignored. Instead, the character objects returned
                inherit from `None` and `nvl` respectively.
            2. `callback`, if defined, will be called after the callback
                defined in this method is called.
        
        The primary reason for this function is to attach to characters
        defined using this method a callback that will manipulate
        global state that keeps track of who the active character is,
        and whether they are speaking. In maintaining this global state,

        1. we make it possible to declaratively define displayables
            associated with characters that display differently
            depending on whether the character is the active character,
            and whether they are speaking.
        2. we make the manipulation between active/inactive and
            speaking/non-speaking automatic with respect to the
            script/scenario. That is, updates to this global state,
            and swapping displayables based on this global state is
            handled automatically without requiring explicit statements
            to change displayables in the script.
        """
        def character_atl_active_inactive_factory(character_objects, tagg=None):
            def pause_while_active(trans, st, at):
                if character_say_state["active"] in character_objects:
                    return 0.2
                else:
                    return None
            def pause_while_inactive(trans, st, at):
                if character_say_state["active"] in character_objects:
                    return None
                else:
                    return 0.2
            return pause_while_active, pause_while_inactive

        def callback_factory():
            state = [None, None]
            def register_character_object(o, callback):
                state[0], state[1] = o, callback
            def callback(event, **kwargs):
                if event == "begin":
                    character_say_state["active"] = state[0]
                elif event == "show":
                    character_say_state["speaking"] = state[0]
                elif event == "show_done":
                    pass
                elif event == "slow_done":
                    character_say_state["speaking"] = False
                elif event == "end":
                    character_say_state["active"] = False
                    character_say_state["speaking"] = False
                if callable(state[1]):
                    return state[1]()
            return register_character_object, callback

        register_adv, adv_callback = callback_factory()
        adv_character = Character(name, callback=adv_callback, *args, **kwargs)
        register_adv(adv_character, callback)
        register_nvl, nvl_callback = callback_factory()
        nvl_character = Character(name, kind=nvl, callback=nvl_callback, *args, **kwargs)
        register_nvl(nvl_character, callback)
        pause_while_active, pause_while_inactive = character_atl_active_inactive_factory([adv_character, nvl_character], tagg=name)
        return adv_character, nvl_character, pause_while_active, pause_while_inactive

define enna_character = character_factory(_("Enna"), color="#858ED1", image="enna")
define en = enna_character[0]
define enn = enna_character[1]

# millie's definitions uses a 1-letter stem so that we define mn and not min which is a Python keyword
define millie_character = character_factory(_("Millie"), color="#FEBC87", image="millie")
define m = millie_character[0]
define mn = millie_character[1]

define young_millie_character = character_factory(_("Young Millie"), color="#FEBC87", image="young_millie")
define ym = young_millie_character[0]
define ymn = young_millie_character[1]

define calamillie_character = character_factory(_("Calamillie"), color="#FEF187", image="calamillie")
define cm = calamillie_character[0]
define cmn = calamillie_character[1]

define reimu_character = character_factory(_("Reimu"), color="#B90B4A", image="reimu")
define re = reimu_character[0]
define ren = reimu_character[1]

define nina_character = character_factory(_("Nina"), color="#FF0000", image="nina")
define ni = nina_character[0]
define nin = nina_character[1]

define lucie_character = character_factory(_("Lucie"), color="#DCACE3", image="lucie")
define lu = lucie_character[0]
define lun = lucie_character[1]

define elira_character = character_factory(_("Elira"), color="#95C8D8", image="elira")
define el = elira_character[0]
define eln = elira_character[1]

define rosemi_character = character_factory(_("Rosemi"), color="#FF80AA", image="rosemi")
define ro = rosemi_character[0]
define ron = rosemi_character[1]

define ike_character = character_factory(_("Ike"), color="#348EC7", image="ike")
define ik = ike_character[0]
define ikn = ike_character[1]

define vox_character = character_factory(_("Vox"), color="#960018", image="vox")
define vo = vox_character[0]
define von = vox_character[1]

define shu_character = character_factory(_("Shu"), color="#A660A7", image="shu")
define sh = shu_character[0]
define shn = shu_character[1]

define agent_from_heaven_character = character_factory(_("Agent from Heaven"), color="#ffffff", image="agent_from_heaven")
define ag = agent_from_heaven_character[0]
define agn = agent_from_heaven_character[1]

define wanderer_character = character_factory(_("Wanderer"), color="#422E5A", image="wanderer")
define wa = wanderer_character[0]
define wan = wanderer_character[1]

define narrator_character = character_factory(None, color="#ffffff")
define narrator = narrator_character[0]
define n = narrator_character[1]
