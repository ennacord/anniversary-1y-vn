init python:
    global_active_characters = set()
    global_speaking_characters = set()
    current_sync_info = None
    lip_sync_timing_info = {}
    lip_sync_info = {}

    class TimingInfo:
        def __init__(self):
            self.started = False
            self.start = -1
            self.next_index = 0

    def voice_lipsynced(voice_file: str, tag: str=None):
        global current_sync_info
        voice_id = voice_file.split('/', 1)[1].split('.')[0]
        current_sync_info = lip_sync_info[voice_id]
        print("set_sync_info", current_sync_info)
        lip_sync_timer = -1
        voice(voice_file, tag)

    def WhenSpeaking(char_id: str, 
                     speaking_sprite: str, speaking_refresh: float, 
                     nonspeaking_sprite: str, nonspeaking_refresh: float):
        def callback(st, at):
            if char_id in global_speaking_characters and renpy.music.is_playing(channel='voice'):
                return speaking_sprite, speaking_refresh
            else:
                return nonspeaking_sprite, nonspeaking_refresh

        return DynamicDisplayable(callback)
    
    def LipSynced(char_id: str, speaking_base: str, nonspeaking_sprite: str):
        print(speaking_base)
        def callback(st, at):
            if char_id not in lip_sync_timing_info:
                lip_sync_timing_info[char_id] = TimingInfo()

            if not (char_id in global_speaking_characters and renpy.music.is_playing(channel='voice') and current_sync_info):
                lip_sync_timing_info[char_id].started = False
                return nonspeaking_sprite, 0.1

            timing_info = lip_sync_timing_info[char_id]
            if not timing_info.started:
                timing_info.started = True
                timing_info.start = st
                timing_info.next_index = 0
            
            if timing_info.next_index < len(current_sync_info):
                next_pos, next_time = current_sync_info[timing_info.next_index]
            else:
                next_pos, next_time = current_sync_info[-1][0], st + 100

            next_pos = speaking_base.format(next_pos)

            if timing_info.next_index == 0:
                prev_pos = nonspeaking_sprite
            else:
                prev_pos = speaking_base.format(current_sync_info[timing_info.next_index - 1][0])

            curr_time = st - lip_sync_timing_info[char_id].start
            if curr_time >= next_time:
                timing_info.next_index += 1
                return next_pos, 0.01
            else:
                return prev_pos, 0.01

        return DynamicDisplayable(callback)


    class CharacterWrapper:
        """
        Returns a tuple containing a character for use in ADV, followed
        by a tuple for use in NVL, given typical parameters to define
        a character using `Character`.

        Presently we assume that all arguments passed for the character
        to be used in ADV are the same for NVL. Here are the changes
        to the way the parameters are handled:
            1. `callback`, if defined, will be called after the callback
                defined in this method is called.
        
        The primary reason for this class is to attach to characters
        defined using this method a callback that will manipulate
        global state that keeps track of who the active character is,
        and whether they are speaking. In maintaining this global state,

        1. we make it possible to declaratively define displayables
            associated with characters that display differently
            depending on whether the character is the active character,
            and whether they are speaking.z
        2. we make the manipulation between active/inactive and
            speaking/non-speaking automatic with respect to the
            script/scenario. That is, updates to (active/inactive,
            speaking/non-speaking) state is handled automatically
            without requiring explicit statements to change displayables
            in the script, and once we write declarative displayables
            to display differently based on this state, we are able to
            swap these displayables in and out based on this state
            without requiring explicit statements to swap displayables
            in the script.
        """
        def __init__(self, ident, name, callback=None, *args, **kwargs):
            self.id = ident
            self.name = name
            self.callback = callback
            self._adv_character = Character(name, callback=self.speech_callback, *args, **kwargs)
            self._nvl_character = Character(name, kind=nvl, callback=self.speech_callback, *args, **kwargs)
            
        def pause_while_active(self, trans, st, at):
            if self.ident in global_active_characters:
                return 0.2
            else:
                return None

        def pause_while_inactive(self, trans, st, at):
            if self.ident in global_active_characters:
                return None
            else:
                return 0.2
            
        def speech_callback(self, event, *args, **kwargs):
            if self.id is not None:
                if event == "begin":
                    global_active_characters.add(self.id)
                elif event == "show":
                    global_speaking_characters.add(self.id)
                elif event == "show_done":
                    pass
                elif event == "slow_done":
                    pass
                    #global_speaking_characters.discard(self.id)
                elif event == "end":
                    global_speaking_characters.discard(self.id)
                    global_active_characters.discard(self.id)

            if callable(self.callback):
                return self.callback(event, *args, **kwargs)
            
        @property
        def adv_character(self):
            return self._adv_character

        @property
        def nvl_character(self):
            return self._nvl_character

define enna_character = CharacterWrapper("enna", _("Enna"), color="#858ED1", image="enna")
define en = enna_character.adv_character
define enn = enna_character.nvl_character

define millie_character = CharacterWrapper("millie", _("Millie"), color="#FEBC87", image="millie")
define ml = millie_character.adv_character
define mln = millie_character.nvl_character

define young_millie_character = CharacterWrapper("young_millie", _("Young Millie"), color="#FEBC87", image="young_millie")
define ym = young_millie_character.adv_character
define ymn = young_millie_character.nvl_character

define calamillie_character = CharacterWrapper("calamillie", _("Calamillie"), color="#FEF187", image="calamillie")
define cm = calamillie_character.adv_character
define cmn = calamillie_character.nvl_character

define reimu_character = CharacterWrapper("reimu", _("Reimu"), color="#B90B4A", image="reimu")
define re = reimu_character.adv_character
define ren = reimu_character.nvl_character

define nina_character = CharacterWrapper("nina", _("Nina"), color="#FF0000", image="nina")
define ni = nina_character.adv_character
define nin = nina_character.nvl_character

define lucie_character = CharacterWrapper("lucie", _("Lucie"), color="#DCACE3", image="lucie")
define lu = lucie_character.adv_character
define lun = lucie_character.nvl_character

define elira_character = CharacterWrapper("elira", _("Elira"), color="#95C8D8", image="elira")
define el = elira_character.adv_character
define eln = elira_character.nvl_character

define rosemi_character = CharacterWrapper("rosemi", _("Rosemi"), color="#FF80AA", image="rosemi")
define ro = rosemi_character.adv_character
define ron = rosemi_character.nvl_character

define ike_character = CharacterWrapper("ike", _("Ike"), color="#348EC7", image="ike")
define ik = ike_character.adv_character
define ikn = ike_character.nvl_character

define vox_character = CharacterWrapper("vox", _("Vox"), color="#960018", image="vox")
define vo = vox_character.adv_character
define von = vox_character.nvl_character

define shu_character = CharacterWrapper("shu", _("Shu"), color="#A660A7", image="shu")
define sh = shu_character.adv_character
define shn = shu_character.nvl_character

define agent_from_heaven_character = CharacterWrapper("agent", _("Agent from Heaven"), color="#ffffff", image="agent_from_heaven")
define ag = agent_from_heaven_character.adv_character
define agn = agent_from_heaven_character.nvl_character

define wanderer_character = CharacterWrapper("wanderer", _("Wanderer"), color="#422E5A", image="wanderer")
define wa = wanderer_character.adv_character
define wan = wanderer_character.nvl_character

define narrator_character = CharacterWrapper(None, None, color="#ffffff")
define narrator = narrator_character.adv_character
define n = narrator_character.nvl_character
