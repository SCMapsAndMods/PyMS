from utils import *
import TBL

import struct, re

THEME_ASSETS_MAIN_MENU = 0x00
THEME_ASSETS_CAMPAIGN = 0x01
THEME_ASSETS_TERRAN_BRIEFING = 0x02
THEME_ASSETS_ZERG_BRIEFING = 0x03
THEME_ASSETS_PROTOSS_BRIEFING = 0x04
THEME_ASSETS_PROTOSS_DEFEAT = 0x05
THEME_ASSETS_PROTOSS_VICTORY = 0x06
THEME_ASSETS_ZERG_DEFEAT = 0x07
THEME_ASSETS_ZERG_VICTORY = 0x08
THEME_ASSETS_TERRAN_DEFEAT = 0x09
THEME_ASSETS_TERRAN_VICTORY = 0x0A
THEME_ASSETS_GENERAL = 0x0B
THEME_ASSETS_NONE = 0x0C
THEME_ASSETS_INFO = {
	THEME_ASSETS_MAIN_MENU: {
		"path":"glue\\palmm\\",
		"name":"Main Menu"
	},
	THEME_ASSETS_CAMPAIGN: {
		"path":"glue\\palcs\\",
		"name":"Campaign"
	},
	THEME_ASSETS_TERRAN_BRIEFING: {
		"path":"glue\\palrt\\",
		"name":"Terran Mission Briefing"
	},
	THEME_ASSETS_ZERG_BRIEFING: {
		"path":"glue\\palrz\\",
		"name":"Zerg Mission Briefing"
	},
	THEME_ASSETS_PROTOSS_BRIEFING: {
		"path":"glue\\palrp\\",
		"name":"Protoss Mission Briefing"
	},
	THEME_ASSETS_PROTOSS_DEFEAT: {
		"path":"glue\\palpd\\",
		"name":"Protoss Defeat"
	},
	THEME_ASSETS_PROTOSS_VICTORY: {
		"path":"glue\\palpv\\",
		"name":"Protoss Victory"
	},
	THEME_ASSETS_ZERG_DEFEAT: {
		"path":"glue\\palzd\\",
		"name":"Zerg Defeat"
	},
	THEME_ASSETS_ZERG_VICTORY: {
		"path":"glue\\palzv\\",
		"name":"Zerg Victory"
	},
	THEME_ASSETS_TERRAN_DEFEAT: {
		"path":"glue\\paltd\\",
		"name":"Terran Defeat"
	},
	THEME_ASSETS_TERRAN_VICTORY: {
		"path":"glue\\paltv\\",
		"name":"Terran Victory"
	},
	THEME_ASSETS_GENERAL: {
		"path":"glue\\palnl\\",
		"name":"General"
	}
}
SCREEN_MAIN_MENU = 0x00
SCREEN_SIMULATE = 0x01
SCREEN_SELCONN = 0x02
SCREEN_CHATROOM = 0x03
SCREEN_BATTLENT = 0x04
SCREEN_LOGIN = 0x05
SCREEN_CAMPAIGN = 0x06
SCREEN_TERRAN_BRIEFING = 0x07
SCREEN_ZERG_BRIEFING = 0x08
SCREEN_PROTOSS_BRIEFING = 0x09
SCREEN_GAMESEL = 0x0A
SCREEN_CREATE = 0x0B
SCREEN_CREATE_2 = 0x0C
SCREEN_LOAD = 0x0D
SCREEN_ZERG_SCORE_DEFEAT = 0x0E
SCREEN_ZERG_SCORE_VICTORY = 0x0F
SCREEN_TERRAN_SCORE_DEFEAT = 0x10
SCREEN_TERRAN_SCORE_VICTORY = 0x11
SCREEN_PROTOSS_SCORE_DEFEAT = 0x12
SCREEN_PROTOSS_SCORE_VICTORY = 0x13
SCREEN_MODEM = 0x14
SCREEN_DIRECT = 0x15
SCREEN_CAMPAIGN_BW = 0x16
SCREEN_GAMEMODE = 0x17
SCREEN_GAMEMODE_2 = 0x18
SCREEN_INFO = {
	SCREEN_MAIN_MENU:{
		# "assets_path":"glue\\mainmenu\\",
		"dialog_bin":"glumain.bin",
		"theme_id":THEME_ASSETS_MAIN_MENU,
		"name":"Main Menu"
	},
	# SCREEN_SIMULATE:{
	# 	# "assets_path":"glue\\simulate",
	# 	"dialog_bin":"",
	# 	"theme_id":THEME_ASSETS_GENERAL,
	# 	"name":""
	# },
	SCREEN_SELCONN:{
		# "assets_path":"glue\\selconn\\",
		"dialog_bin":"gluconn.bin",
		"theme_id":THEME_ASSETS_GENERAL,
		"name":"Multiplay Connection Selection"
	},
	SCREEN_CHATROOM:{
		# "assets_path":"glue\\chatroom\\",
		"dialog_bin":"gluchat.bin",
		"theme_id":THEME_ASSETS_GENERAL,
		"name":"Game Lobby"
	},
	# SCREEN_BATTLENT:{
	# 	# "assets_path":"glue\\battle.net\\",
	# 	"dialog_bin":"",
	# 	"theme_id":THEME_ASSETS_NONE,
	# 	"name":""
	# },
	SCREEN_LOGIN:{
		# "assets_path":"glue\\login\\",
		"dialog_bin":"glulogin.bin",
		"theme_id":THEME_ASSETS_GENERAL,
		"name":"Username Selection"
	},
	SCREEN_CAMPAIGN:{
		# "assets_path":"glue\\campaign\\",
		"dialog_bin":"glucmpgn.bin",
		"theme_id":THEME_ASSETS_CAMPAIGN,
		"name":"Campaign Selection"
	},
	SCREEN_TERRAN_BRIEFING:{
		# "assets_path":"glue\\ReadyT\\",
		"dialog_bin":"glurdyt.bin",
		"theme_id":THEME_ASSETS_TERRAN_BRIEFING,
		"name":"Terran Mission Briefing"
	},
	SCREEN_ZERG_BRIEFING:{
		# "assets_path":"glue\\ReadyZ\\",
		"dialog_bin":"glurdyz.bin",
		"theme_id":THEME_ASSETS_ZERG_BRIEFING,
		"name":"Zerg Mission Briefing"
	},
	SCREEN_PROTOSS_BRIEFING:{
		# "assets_path":"glue\\ReadyP\\",
		"dialog_bin":"glurdyp.bin",
		"theme_id":THEME_ASSETS_PROTOSS_BRIEFING,
		"name":"Protoss Mission Briefing"
	},
	SCREEN_GAMESEL:{
		# "assets_path":"glue\\gamesel\\",
		"dialog_bin":"glujoin.bin",
		"theme_id":THEME_ASSETS_GENERAL,
		"name":"Games List"
	},
	SCREEN_CREATE:{
		# "assets_path":"glue\\create\\",
		"dialog_bin":"glucreat.bin",
		"theme_id":THEME_ASSETS_GENERAL,
		"name":"Create Game (Multiplayer)"
	},
	SCREEN_CREATE_2:{
		# "assets_path":"glue\\create\\",
		"dialog_bin":"glucustm.bin",
		"theme_id":THEME_ASSETS_GENERAL,
		"name":"Create Game (Singleplayer)"
	},
	SCREEN_LOAD:{
		# "assets_path":"glue\\load\\",
		"dialog_bin":"gluload.bin",
		"theme_id":THEME_ASSETS_GENERAL,
		"name":"Save Games"
	},
	SCREEN_ZERG_SCORE_DEFEAT:{
		# "assets_path":"glue\\score\\",
		"dialog_bin":"gluscore.bin",
		"theme_id":THEME_ASSETS_ZERG_DEFEAT,
		"name":"Zerg Score Screen (Defeat)"
	},
	SCREEN_ZERG_SCORE_VICTORY:{
		# "assets_path":"glue\\score\\",
		"dialog_bin":"gluscore.bin",
		"theme_id":THEME_ASSETS_ZERG_VICTORY,
		"name":"Zerg Score Screen (Victory)"
	},
	SCREEN_TERRAN_SCORE_DEFEAT:{
		# "assets_path":"glue\\score\\",
		"dialog_bin":"gluscore.bin",
		"theme_id":THEME_ASSETS_TERRAN_DEFEAT,
		"name":"Terran Score Screen (Defeat)"
	},
	SCREEN_TERRAN_SCORE_VICTORY:{
		# "assets_path":"glue\\score\\",
		"dialog_bin":"gluscore.bin",
		"theme_id":THEME_ASSETS_TERRAN_VICTORY,
		"name":"Terran Score Screen (Victory)"
	},
	SCREEN_PROTOSS_SCORE_DEFEAT:{
		# "assets_path":"glue\\score\\",
		"dialog_bin":"gluscore.bin",
		"theme_id":THEME_ASSETS_PROTOSS_DEFEAT,
		"name":"Protoss Score Screen (Defeat)"
	},
	SCREEN_PROTOSS_SCORE_VICTORY:{
		# "assets_path":"glue\\score\\",
		"dialog_bin":"gluscore.bin",
		"theme_id":THEME_ASSETS_PROTOSS_VICTORY,
		"name":"Protoss Score Screen (Victory)"
	},
	SCREEN_MODEM:{
		# "assets_path":"glue\\modem\\",
		"dialog_bin":"glumodem.bin",
		"theme_id":THEME_ASSETS_GENERAL,
		"name":"Modem Connection"
	},
	# SCREEN_DIRECT:{
	# 	# "assets_path":"glue\\direct\\",
	# 	"dialog_bin":"",
	# 	"theme_id":THEME_ASSETS_GENERAL,
	# 	"name":""
	# },
	SCREEN_CAMPAIGN_BW:{
		# "assets_path":"glue\\campaign\\",
		"dialog_bin":"gluexpcmpgn.bin",
		"theme_id":THEME_ASSETS_CAMPAIGN,
		"name":"Campaign Selection (BroodWar)"
	},
	# SCREEN_GAMEMODE:{
	# 	# "assets_path":"glue\\gamemode\\",
	# 	"dialog_bin":"",
	# 	"theme_id":THEME_ASSETS_GENERAL,
	# 	"name":""
	# },
	# SCREEN_GAMEMODE_2:{
	# 	# "assets_path":"glue\\gamemode\\",
	# 	"dialog_bin":"",
	# 	"theme_id":THEME_ASSETS_GENERAL,
	# 	"name":""
	# },
}
DIALOG_ASSETS = {
	
}

class BINWidget(object):
	BYTE_SIZE = 86
	ATTR_NAMES = ('x1','y1','x2','y2','width','height','unknown1','string','flags','unknown2','identifier','type','unknown3','unknown4','unknown5','unknown6','responsive_x1','responsive_y1','responsive_x2','responsive_y2','unknown7','smk','text_offset_x','text_offset_y','responsive_width','responsive_height','unknown8','unknown9')

	FLAG_UNK1 = 0x00000001
	FLAG_DISABLED = 0x00000002
	FLAG_UNK2 = 0x00000004
	FLAG_VISIBLE = 0x00000008
	FLAG_RESPONSIVE = 0x00000010
	FLAG_UNK3 = 0x00000020
	FLAG_CANCEL_BTN = 0x00000040
	FLAG_NO_HOVER_SND = 0x00000080
	FLAG_VIRTUAL_HOTKEY = 0x00000100
	FLAG_HAS_HOTKEY = 0x00000200
	FLAG_FONT_SIZE_10 = 0x00000400
	FLAG_FONT_SIZE_16 = 0x00000800
	FLAG_UNK4 = 0x00001000
	FLAG_TRANSPARENCY = 0x00002000
	FLAG_FONT_SIZE_16x = 0x00004000
	FLAG_UNK5 = 0x00008000
	FLAG_FONT_SIZE_14 = 0x00010000
	FLAG_UNK6 = 0x00020000
	FLAG_TRANSLUCENT = 0x00040000
	FLAG_DEFAULT_BTN = 0x00080000
	FLAG_ON_TOP = 0x00100000
	FLAG_TEXT_ALIGN_CENTER = 0x00200000
	FLAG_TEXT_ALIGN_RIGHT = 0x00400000
	FLAG_TEXT_ALIGN_CENTER2 = 0x00800000
	FLAG_ALIGN_TOP = 0x01000000
	FLAG_ALIGN_MIDDLE = 0x02000000
	FLAG_ALIGN_BOTTOM = 0x04000000
	FLAG_UNK7 = 0x08000000
	FLAG_UNK8 = 0x10000000
	FLAG_UNK9 = 0x20000000
	FLAG_NO_CLICK_SND = 0x40000000
	FLAG_UNK10 = 0x80000000

	FLAGS_TEXT_ALIGN = (FLAG_TEXT_ALIGN_CENTER | FLAG_TEXT_ALIGN_RIGHT | FLAG_TEXT_ALIGN_CENTER2)

	TYPE_DIALOG = 0
	TYPE_DEFAULT_BTN = 1
	TYPE_BUTTON = 2
	TYPE_OPTION_BTN = 3
	TYPE_CHECKBOX = 4
	TYPE_IMAGE = 5
	TYPE_SLIDER = 6
	TYPE_UNK = 7
	TYPE_TEXTBOX = 8
	TYPE_LABEL_LEFT_ALIGN = 9
	TYPE_LABEL_CENTER_ALIGN = 10
	TYPE_LABEL_RIGHT_ALIGN = 11
	TYPE_LISTBOX = 12
	TYPE_COMBOBOX = 13
	TYPE_HIGHLIGHT_BTN = 14

	INTERFACE_ID = 65535

	TYPE_NAMES = ['Dialog','Deafult Button','Button','Option Button','CheckBox','Image','Slider','Unknown','TextBox','Label (Left Align)','Label (Right Align)','Label (Center Align)','ListBox','ComboBox','Highlight Button']

	def __init__(self, ctrl_type=TYPE_DIALOG):
		self.x1 = 0
		self.y1 = 0
		self.x2 = 0
		self.y2 = 0
		self.width = 0
		self.height = 0
		self.unknown1 = 0
		self.string = ''
		self.flags = BINWidget.FLAG_VISIBLE
		self.unknown2 = 0
		self.identifier = BINWidget.INTERFACE_ID
		BINWidget.INTERFACE_ID -= 1
		self.type = ctrl_type
		self.unknown3 = 0
		self.unknown4 = 0
		self.unknown5 = 0
		self.unknown6 = 0
		self.responsive_x1 = 0
		self.responsive_y1 = 0
		self.responsive_x2 = 0
		self.responsive_y2 = 0
		self.unknown7 = 0
		self.smk = None
		self.text_offset_x = 0
		self.text_offset_y = 0
		self.responsive_width = 0
		self.responsive_height = 0
		self.unknown8 = 0
		self.unknown9 = 0
		if self.type in (BINWidget.TYPE_DEFAULT_BTN, BINWidget.TYPE_BUTTON, BINWidget.TYPE_OPTION_BTN, BINWidget.TYPE_SLIDER, BINWidget.TYPE_TEXTBOX, BINWidget.TYPE_LISTBOX, BINWidget.TYPE_COMBOBOX, BINWidget.TYPE_HIGHLIGHT_BTN):
			self.flags |= BINWidget.FLAG_RESPONSIVE

	def bounding_box(self):
		x1 = (self.x1 if self.x1 < self.x2 else self.x2)
		y1 = (self.y1 if self.y1 < self.y2 else self.y2)
		x2 = (self.x2 if self.x2 > self.x1 else self.x1)
		y2 = (self.y2 if self.y2 > self.y1 else self.y1)
		return [x1,y1,x2,y2]

	def text_box(self):
		box = self.bounding_box()
		box[0] += self.text_offset_x
		box[1] += self.text_offset_y
		return box

	def has_responsive(self):
		return (self.flags & BINWidget.FLAG_RESPONSIVE == BINWidget.FLAG_RESPONSIVE) #(self.responsive_x1 or self.responsive_y1 or self.responsive_x2 or self.responsive_y2)

	def responsive_box(self):
		box = self.bounding_box()
		box[0] += self.responsive_x1
		box[1] += self.responsive_y1
		box[2] = box[0] + self.responsive_x2
		box[3] = box[1] + self.responsive_y2
		return box

	def display_text(self):
		if self.type != BINWidget.TYPE_DIALOG and self.type != BINWidget.TYPE_IMAGE:
			if self.flags & (BINWidget.FLAG_VIRTUAL_HOTKEY | BINWidget.FLAG_HAS_HOTKEY):
				return self.string[1:]
			else:
				return self.string
		return None

class BINSMK(object):
	BYTE_SIZE = 30
	ATTR_NAMES = ('overlay_smk','flags','unknown1','filename','unknown2','offset_x','offset_y','unknown3','unknown4')

	FLAG_FADE_IN = 0x0001
	FLAG_DARK = 0x0002
	FLAG_REPEATS = 0x0004
	FLAG_SHOW_ON_HOVER = 0x0008
	FLAG_UNK = 0x0010

	def __init__(self):
		self.widgets = []
		self.overlay_smk = None
		self.flags = 0
		self.unknown1 = 0
		self.filename = ''
		self.unknown2 = 0
		self.offset_x = 0
		self.offset_y = 0
		self.unknown3 = 0
		self.unknown4 = 0

	def add_widget(self, widget):
		self.widgets.append(widget)

	def remove_widget(self, widget):
		self.widget.remove(widget)

class DialogBIN:
	def __init__(self):
		dialog = BINWidget()
		dialog.x2 = 639
		dialog.y2 = 479
		dialog.width = 640
		dialog.height = 480
		self.widgets = [dialog]
		self.smks = []

	def load_file(self, file):
		try:
			if isstr(file):
				f = open(file,'rb')
				data = f.read()
				f.close()
			else:
				data = file.read()
		except:
			raise PyMSError('Load',"Could not load Dialog BIN file '%s'" % file)
		try:
			self.load_data(data)
		except PyMSError, e:
			raise e
		except:
			raise
			raise PyMSError('Load',"Unsupported Dialog BIN file '%s', could possibly be corrupt" % file)

	def load_data(self, data):
		widgets = []
		smk_map = {}
		smks = []
		def load_smk(offset):
			smk_info = list(struct.unpack('<LH3LHHLL',data[offset:offset+BINSMK.BYTE_SIZE]))
			filename_offset = smk_info[3]
			end_offset = data.find('\0', filename_offset)
			smk_info[3] = data[filename_offset:end_offset]
			smk = BINSMK()
			smk_map[offset] = smk
			smks.append(smk)
			overlay_smk_offset = smk_info[0]
			if overlay_smk_offset:
				if not overlay_smk_offset in smk_map:
					load_smk(overlay_smk_offset)
				smk_info[0] = smk_map[overlay_smk_offset]
			else:
				smk_info[0] = None
			attrs = BINSMK.ATTR_NAMES
			for attr,value in zip(attrs,smk_info):
				setattr(smk, attr, value)
		def load_widget(offset):
			widget_info = list(struct.unpack('<L6H4LH5L4HLL4HLL',data[offset:offset+BINWidget.BYTE_SIZE]))
			string_offset = widget_info[8]
			if string_offset:
				end_offset = data.find('\0', string_offset)
				widget_info[8] = data[string_offset:end_offset]
			else:
				widget_info[8] = ''
			next_widget = widget_info[0]
			smk_offset = widget_info[22]
			if widget_info[11] == BINWidget.TYPE_DIALOG:
				next_widget = smk_offset
				smk_offset = 0
			if smk_offset:
				if not smk_offset in smk_map:
					load_smk(smk_offset)
				widget_info[22] = smk_map[smk_offset]
			else:
				widget_info[22] = None
			widget = BINWidget()
			attrs = BINWidget.ATTR_NAMES
			for attr,value in zip(attrs,widget_info[1:]):
				setattr(widget, attr, value)
			if widget.type == BINWidget.TYPE_DIALOG:
				widget.x2 = widget.x1 + widget.responsive_x1
				widget.y2 = widget.y1 + widget.responsive_y1
			else:
				widget.x1 += widgets[0].x1
				widget.y1 += widgets[0].y1
				widget.x2 += widgets[0].x1
				widget.y2 += widgets[0].y1
			widgets.append(widget)
			if next_widget:
				load_widget(next_widget)
		load_widget(0)
		self.widgets = widgets
		self.smks = smks

	def save_file(self, file):
		try:
			f = AtomicWriter(file, 'wb')
		except:
			raise
		f.write(self.save_data())
		f.close()

	def save_data(self):
		smk_offsets = {}
		string_offsets = {}
		smk_offset = len(self.widgets) * BINWidget.BYTE_SIZE
		offsets = [0, smk_offset, smk_offset + len(self.smks) * BINSMK.BYTE_SIZE]
		results = ['','','']
		def save_string(string):
			if not string:
				return 0
			if not string in string_offsets:
				string_offsets[string] = offsets[2]
				offsets[2] += len(string) + 1
				results[2] += string + '\0'
			return string_offsets[string]
		def save_smk(smk):
			data = ''
			if not smk in smk_offsets:
				smk_offsets[smk] = offsets[1]
				offsets[1] += BINSMK.BYTE_SIZE
				smk_info = []
				attrs = BINSMK.ATTR_NAMES
				for attr in attrs:
					value = getattr(smk, attr)
					if attr == 'overlay_smk' and value != None:
						value,data = save_smk(value)
					elif attr == 'filename':
						value = save_string(value)
					if value == None:
						value = 0
					smk_info.append(value)
				data = struct.pack('<LH3LHHLL', *smk_info) + data
			return (smk_offsets[smk],data)
		def save_widget(widget, next_offset):
			widget_info = []
			if widget == last_widget or widget.type == BINWidget.TYPE_DIALOG:
				widget_info.append(0)
			else:
				widget_info.append(next_offset)
			attrs = BINWidget.ATTR_NAMES
			for attr in attrs:
				value = getattr(widget, attr)
				if attr == 'string':
					value = save_string(value)
				elif attr == 'smk':
					if widget.type == BINWidget.TYPE_DIALOG:
						value = next_offset
					elif value != None:
						value,data = save_smk(value)
						results[1] += data
				elif widget.type == BINWidget.TYPE_DIALOG:
					if attr == 'x2':
						value = widget.width-1
					elif attr == 'y2':
						value = widget.height-1
					elif attr == 'responsive_x1':
						value = widget.width
					elif attr == 'responsive_y1':
						value = widget.height
				elif attr in ('x1','x2'):
					value -= self.widgets[0].x1
				elif attr in ('y1','y2'):
					value -= self.widgets[0].y1
				if value == None:
					value = 0
				widget_info.append(value)
			offsets[0] += BINWidget.BYTE_SIZE
			results[0] += struct.pack('<L6H4LH5L4HLL4HLL', *widget_info)
		last_widget = self.widgets[-1]
		for widget in self.widgets:
			next_offset = offsets[0] + BINWidget.BYTE_SIZE
			if widget == last_widget:
				next_offset = 0
			save_widget(widget, next_offset)
		return ''.join(results)

	def interpret_file(self, file):
		try:
			if isstr(file):
				f = open(file,'rb')
				data = f.read()
				f.close()
			else:
				data = file.read()
		except:
			raise PyMSError('Load',"Could not load file '%s'" % file)
		self.interpret_data(data)

	def interpret_data(self, data):
		lines = re.split('(?:\r?\n)+', data)
		widgets = []
		smks = {}
		backfill_smks = {}
		working = None
		def get_smk(smk_id):
			smk = None
			if smk_id in smks:
				smk = smks[smk_id]
			else:
				if not smk_id in backfill_smks:
					backfill_smks[smk_id] = []
				backfill_smks[smk_id].append(working)
			return smk
		for n,raw_line in enumerate(lines):
			line = raw_line.split('#',1)[0].strip()
			if not line:
				continue
			if line == 'Widget:':
				working = BINWidget()
				widgets.append(working)
				continue
			m = re.match('^SMK (\d+):$', line)
			if m:
				smk_id = int(m.group(1))
				if smk_id in smks:
					raise PyMSError('Interpreting',"Duplicate definition for SMK '%s'" % attr,n,line)
				working = BINSMK()
				if smk_id in backfill_smks:
					for obj in backfill_smks[smk_id]:
						if isinstance(obj, BINWidget):
							obj.smk = working
						else:
							obj.overlay_smk = working
					del backfill_smks[smk_id]
				smks[smk_id] = working
				continue
			if not working:
				raise PyMSError('Interpreting','Unexpected line, expected a Widget or SMK header',n,line)
			m = re.match('^(\S+)(?:\s+(.+))?$', line)
			attr = m.group(1)
			value = m.group(2)
			if isinstance(working, BINWidget):
				if not attr in BINWidget.ATTR_NAMES:
					raise PyMSError('Interpreting',"Invalid Widget attribute name '%s'" % attr,n,line)
				if attr == 'smk':
					if value == 'None':
						value = None
					else:
						try:
							smk_id = int(value)
						except:
							raise PyMSError('Interpreting',"Invalid SMK id '%s', expected an Integer or 'None'" % value,n,line)
						value = get_smk(smk_id)
				elif attr == 'string':
					if value == None:
						value = ''
					else:
						value = TBL.compile_string(value)
				elif attr == 'flags':
					# todo: try catch
					value = flags(value, 27)
				else:
					# todo: try catch
					value = int(value)
			else:
				if not attr in BINSMK.ATTR_NAMES:
					raise PyMSError('Interpreting',"Invalid SMK attribute name '%s'" % attr,n,line)
				if attr == 'overlay_smk':
					if value == 'None':
						value = None
					else:
						try:
							smk_id = int(value)
						except:
							raise PyMSError('Interpreting',"Invalid SMK id '%s', expected an Integer or 'None'" % value,n,line)
						value = get_smk(smk_id)
				elif attr == 'filename':
					value = TBL.compile_string(value)
				elif attr == 'flags':
					value = flags(value, 5)
				else:
					value = int(value)
			setattr(working, attr, value)
		if backfill_smks:
			raise PyMSError('Interpreting',"SMK %s is missing" % backfill_smks.keys()[0])
		for i in xrange(len(widgets)):
			widget = widgets[i]
			if widget.type == BINWidget.TYPE_DIALOG:
				del widgets[i]
				widgets.insert(i,widget)
				break
		else:
			raise PyMSError('Interpreting','No dialog found.')
		self.widgets = widgets
		self.smks = list(smk for i,smk in sorted(smks.iteritems(),key=lambda s: s[1]))

	def decompile_file(self, file):
		try:
			f = AtomicWriter(file, 'wb')
		except:
			raise
		f.write(self.decompile_data())
		f.close()

	def decompile_data(self):
		result = ''
		attrs = BINSMK.ATTR_NAMES
		longest = sorted(len(n) for n in attrs)[-1]
		for i,smk in enumerate(self.smks):
			result += 'SMK %d:\n' % i
			for attr in attrs:
				value = getattr(smk, attr)
				hint = ''
				if attr == 'overlay_smk' and value != None:
					value = self.smks.index(value)
				elif attr == 'filename':
					value = TBL.decompile_string(value)
				elif attr == 'flags':
					value = flags(value, 5)
				result += '\t%s%s%s%s%s\n' % (attr,' ' * (longest - len(attr) + 1),value,' # ' if hint else '',hint)
			result += '\n'
		attrs = BINWidget.ATTR_NAMES
		longest = sorted(len(n) for n in attrs)[-1]
		for widget in self.widgets:
			result += 'Widget:\n'
			for attr in attrs:
				value = getattr(widget, attr)
				hint = ''
				if attr == 'smk' and value != None:
					value = self.smks.index(value)
				elif attr == 'string' and value != None:
					value = TBL.decompile_string(value)
				elif attr == 'flags':
					value = flags(value, 27)
				elif attr == 'type':
					if value < len(BINWidget.TYPE_NAMES):
						hint = BINWidget.TYPE_NAMES[value]
					else:
						hint = 'Unknown'
				result += '\t%s%s%s%s%s\n' % (attr,' ' * (longest - len(attr) + 1),value,' # ' if hint else '',hint)
			result += '\n'
		return result

# if __name__ == '__main__':
# 	dialogbin = DialogBIN()
# 	dialogbin.load_file('/Users/zachzahos/Documents/Projects/PyMS/Libs/WORKING/rez/glumain.bin')
# 	data = dialogbin.save_data()
# 	dialogbin.load_data(data)
# 	dialogbin.decompile_file('/Users/zachzahos/Documents/Projects/PyMS/Libs/WORKING/rez/glumain.txt')
# 	dialogbin.interpret_file('/Users/zachzahos/Documents/Projects/PyMS/Libs/WORKING/rez/glumain.txt')
# 	data = dialogbin.save_data()
# 	dialogbin.load_data(data)
# 	dialogbin.decompile_file('/Users/zachzahos/Documents/Projects/PyMS/Libs/WORKING/rez/glumain2.txt')

