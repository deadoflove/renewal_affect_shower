# Search:

import uiToolTip

#add:

if app.ENABLE_RENEWAL_AFFECT_SHOWER:
	import uiCommon, net
	# Define priority lists
	PRIORITY_FIRST = {
		chr.NEW_AFFECT_AUTO_HP_RECOVERY,
		chr.NEW_AFFECT_AUTO_SP_RECOVERY,
		chr.AFFECT_ATT_SPEED_POTION,
		chr.AFFECT_MOV_SPEED_POTION,
	}  # These items will appear first

	PRIORITY_LAST = {
		chr.NEW_AFFECT_POLYMORPH,
	}  # These elements will appear at the end

# Search:

class LovePointImage(ui.ExpandedImageBox):

# within the class LovePointImage search

	def OnMouseOverIn(self):
		self.toolTip.ShowToolTip()

#add

		if app.ENABLE_RENEWAL_AFFECT_SHOWER:
			self.SetScale(0.9,0.9)

# Search:

class LovePointImage(ui.ExpandedImageBox):

# within the class LovePointImage search

	def OnMouseOverOut(self):
		self.toolTip.HideToolTip()

#add

		if app.ENABLE_RENEWAL_AFFECT_SHOWER:
			self.SetScale(0.7, 0.7)


# Search:

class HorseImage(ui.ExpandedImageBox):

# within the class HorseImage search

	def OnMouseOverIn(self):
		#for textLine in self.textLineList:
		#	textLine.Show()

		self.toolTip.ShowToolTip()

# add:

		if app.ENABLE_RENEWAL_AFFECT_SHOWER:
			self.SetScale(0.9,0.9)

# Search:

class HorseImage(ui.ExpandedImageBox):

# within the class HorseImage search

	def OnMouseOverOut(self):
		#for textLine in self.textLineList:
		#	textLine.Hide()

		self.toolTip.HideToolTip()

# add:

		if app.ENABLE_RENEWAL_AFFECT_SHOWER:
			self.SetScale(0.7, 0.7)


# Search:

class AutoPotionImage(ui.ExpandedImageBox):

#removes the class it is not necessary to use it, it is preferable if you want to keep unused code.

# update, set your old class to else:

class AffectImage(ui.ExpandedImageBox):

# replace

iif app.ENABLE_RENEWAL_AFFECT_SHOWER:
	class AffectImage(ui.ExpandedImageBox):
		NORMAL_COLOR = 0xffC5C7C4
		BONUS_COLOR = 0xff95A693
		WHITE_COLOR = 0xffffffff
		def __init__(self):
			ui.ExpandedImageBox.__init__(self)
			self.toolTip = uiToolTip.ToolTip()
			self.toolTip.HideToolTip()
			self.isToolTipVisible = False
			self.skillIndex = None
			self.priority = 0
			self.Canberemoved = False
			self.isSkillAffect = True
			self.description = None
			self.endTime = 0
			self.affect = None

		def SetCanberemoved(self, Canberemoved):
			self.Canberemoved = Canberemoved

		def SetPriority(self, priority):
			self.priority = priority

		def GetPriority(self):
			return self.priority

		def SetAffect(self, affect):
			self.affect = affect

		def GetAffect(self):
			return self.affect

		def SetToolTipText(self, text):
			if hasattr(self, "currentToolTipText") and self.currentToolTipText == text:
				return

			self.toolTip.ClearToolTip()
			self.toolTip.AutoAppendTextLine(text, self.WHITE_COLOR)
			if self.Canberemoved:
				self.toolTip.AutoAppendTextLine(localeInfo.AFFECTSHOWER_REMOVE_TEXT, self.NORMAL_COLOR)
			self.toolTip.AlignHorizonalCenter()
			self.toolTip.ResizeToolTip()
			self.currentToolTipText = text

		def SetDescription(self, description):
			self.description = description
			self.UpdateDescription()

		def SetDuration(self, duration):
			self.endTime = 0
			if duration > 0:
				self.endTime = app.GetGlobalTimeStamp() + duration
				self.UpdateDescription()

		def UpdateAutoPotionDescription(self):
			if not self.toolTip:
				return

			potionType = 0
			if self.affect == chr.NEW_AFFECT_AUTO_HP_RECOVERY:
				potionType = player.AUTO_POTION_TYPE_HP
				PotionName = localeInfo.TOOLTIP_AUTO_POTION_HP
			else:
				potionType = player.AUTO_POTION_TYPE_SP
				PotionName = localeInfo.TOOLTIP_AUTO_POTION_SP

			isActivated, currentAmount, totalAmount, slotIndex = player.GetAutoPotionInfo(potionType)

			amountPercent = 0.0

			try:
				amountPercent = (float(currentAmount) / totalAmount) * 100.0
			except:
				amountPercent = 100.0

			self.toolTip.ClearToolTip()
			self.toolTip.AutoAppendTextLine(PotionName, self.WHITE_COLOR)
			self.toolTip.AutoAppendTextLine(self.description % amountPercent, self.NORMAL_COLOR)
			self.toolTip.AlignHorizonalCenter()
			self.toolTip.ResizeToolTip()

		def UpdateDescription(self):
			if not self.toolTip:
				return

			if not self.description:
				return

			self.toolTip.ClearToolTip()
			self.toolTip.AutoAppendTextLine(self.description, self.WHITE_COLOR)

			if self.endTime > 0:
				remaining_time = self.endTime - app.GetGlobalTimeStamp()
				leftTime = localeInfo.FormatTime(remaining_time)
				timeText = "(%s : %s)" % (localeInfo.LEFT_TIME, leftTime)
				self.toolTip.AutoAppendTextLine(timeText, self.NORMAL_COLOR)

			if self.Canberemoved:
				self.toolTip.AutoAppendTextLine(localeInfo.AFFECTSHOWER_REMOVE_TEXT, self.NORMAL_COLOR)

			self.toolTip.AlignHorizonalCenter()
			self.toolTip.ResizeToolTip()

		def SetSkillIndex(self, skillIndex):
			self.skillIndex = skillIndex

		def UpdateSkillDescription(self):
			if self.skillIndex is None:
				return

			slotIndex = player.GetSkillSlotIndex(self.skillIndex)
			skillCurrentPercentage = player.GetSkillCurrentEfficientPercentage(slotIndex)
			self.toolTip.ClearToolTip()

			skillName = skill.GetSkillName(self.skillIndex)
			self.toolTip.AutoAppendTextLine(skillName, self.WHITE_COLOR)

			for i in xrange(skill.GetSkillAffectDescriptionCount(self.skillIndex)):
				description = skill.GetSkillAffectDescription(self.skillIndex, i, skillCurrentPercentage)
				self.toolTip.AutoAppendTextLine(description, self.BONUS_COLOR)

			if self.endTime > 0:
				remaining_time = self.endTime - app.GetGlobalTimeStamp()
				leftTime = localeInfo.FormatTime(remaining_time)
				timeText = "(%s : %s)" % (localeInfo.LEFT_TIME, leftTime)
				self.toolTip.AutoAppendTextLine(timeText, self.NORMAL_COLOR)

			if self.Canberemoved:
				self.toolTip.AutoAppendTextLine(localeInfo.AFFECTSHOWER_REMOVE_TEXT, self.NORMAL_COLOR)

			self.toolTip.AlignHorizonalCenter()
			self.toolTip.ResizeToolTip()

		def SetSkillAffectFlag(self, flag):
			self.isSkillAffect = flag

		def IsSkillAffect(self):
			return self.isSkillAffect

		def OnMouseOverIn(self):
			self.SetScale(0.9,0.9)
			if self.toolTip:
				self.toolTip.ShowToolTip()
				self.isToolTipVisible = True

		def OnMouseOverOut(self):
			self.SetScale(0.7,0.7)
			if self.toolTip:
				self.toolTip.HideToolTip()
				self.isToolTipVisible = False
else:
else:
	class AffectImage(ui.ExpandedImageBox):

		def __init__(self):
			ui.ExpandedImageBox.__init__(self)

			self.toolTipText = None
			self.isSkillAffect = True
			self.description = None
			self.endTime = 0
			self.affect = None
			self.isClocked = True

		def SetAffect(self, affect):
			self.affect = affect

		def GetAffect(self):
			return self.affect

		def SetToolTipText(self, text, x = 0, y = -19):

			if not self.toolTipText:
				textLine = ui.TextLine()
				textLine.SetParent(self)
				textLine.SetSize(0, 0)
				textLine.SetOutline()
				textLine.Hide()
				self.toolTipText = textLine

			self.toolTipText.SetText(text)
			w, h = self.toolTipText.GetTextSize()
			if localeInfo.IsARABIC():
				self.toolTipText.SetPosition(w+20, y)
			else:
				self.toolTipText.SetPosition(max(0, x + self.GetWidth()/2 - w/2), y)

		def SetDescription(self, description):
			self.description = description

		def SetDuration(self, duration):
			self.endTime = 0
			if duration > 0:
				self.endTime = app.GetGlobalTimeStamp() + duration

		def UpdateAutoPotionDescription(self):

			potionType = 0
			if self.affect == chr.NEW_AFFECT_AUTO_HP_RECOVERY:
				potionType = player.AUTO_POTION_TYPE_HP
			else:
				potionType = player.AUTO_POTION_TYPE_SP

			isActivated, currentAmount, totalAmount, slotIndex = player.GetAutoPotionInfo(potionType)

			#print "UpdateAutoPotionDescription ", isActivated, currentAmount, totalAmount, slotIndex

			amountPercent = 0.0

			try:
				amountPercent = (float(currentAmount) / totalAmount) * 100.0
			except:
				amountPercent = 100.0

			self.SetToolTipText(self.description % amountPercent, 0, 40)

		def SetClock(self, isClocked):
			self.isClocked = isClocked

		def UpdateDescription(self):
			if not self.isClocked:
				self.__UpdateDescription2()
				return

			if not self.description:
				return

			toolTip = self.description
			if self.endTime > 0:
				leftTime = localeInfo.SecondToDHM(self.endTime - app.GetGlobalTimeStamp())
				toolTip += " (%s : %s)" % (localeInfo.LEFT_TIME, leftTime)
			self.SetToolTipText(toolTip, 0, 40)

		def __UpdateDescription2(self):
			if not self.description:
				return

			toolTip = self.description
			self.SetToolTipText(toolTip, 0, 40)

		def SetSkillAffectFlag(self, flag):
			self.isSkillAffect = flag

		def IsSkillAffect(self):
			return self.isSkillAffect

		def OnMouseOverIn(self):
			if self.toolTipText:
				self.toolTipText.Show()

		def OnMouseOverOut(self):
			if self.toolTipText:
				self.toolTipText.Hide()

# Search:
	MALL_DESC_IDX_START = 1000

# add
	if app.ENABLE_RENEWAL_AFFECT_SHOWER:
		WATER_DESC_IDX_START = 1200
		DEW_DESC_IDX_START = 1400
		DEW_RANGE_OFFSET = 200
		TOOLTIP_UPDATE_INTERVAL = 500
		MAX_ITEMS_PER_ROW = 10

# search:

	if app.ENABLE_DRAGON_SOUL_SYSTEM:
		AFFECT_DATA_DICT[chr.NEW_AFFECT_DRAGON_SOUL_DECK1] = (localeInfo.TOOLTIP_DRAGON_SOUL_DECK1, "d:/ymir work/ui/dragonsoul/buff_ds_sky1.tga")
		AFFECT_DATA_DICT[chr.NEW_AFFECT_DRAGON_SOUL_DECK2] = (localeInfo.TOOLTIP_DRAGON_SOUL_DECK2, "d:/ymir work/ui/dragonsoul/buff_ds_land1.tga")
	if app.ENABLE_WOLFMAN_CHARACTER:
		AFFECT_DATA_DICT[chr.AFFECT_BLEEDING] = (localeInfo.SKILL_BLEEDING, "d:/ymir work/ui/skill/common/affect/poison.sub")
		AFFECT_DATA_DICT[chr.AFFECT_RED_POSSESSION] = (localeInfo.SKILL_GWIGEOM, "d:/ymir work/ui/skill/wolfman/red_possession_03.sub")
		AFFECT_DATA_DICT[chr.AFFECT_BLUE_POSSESSION] = (localeInfo.SKILL_CHEONGEUN, "d:/ymir work/ui/skill/wolfman/blue_possession_03.sub")

# add:

	if app.ENABLE_RENEWAL_AFFECT_SHOWER:
		AFFECT_DATA_DICT[chr.NEW_AFFECT_POLYMORPH] =  (localeInfo.POLYMORPH_AFFECT_TOOLTIP, "icon/item/70104.tga")



# Search:

	def __init__(self):
		ui.Window.__init__(self)

# add before

	if app.ENABLE_RENEWAL_AFFECT_SHOWER:
		def Show(self):
			ui.Window.Show(self)
			self.SyncAffectImages()

#search:

	def __init__(self):

#inside, look

		self.lovePointImage=None
		
#add:

		if app.ENABLE_RENEWAL_AFFECT_SHOWER:
			self.RemoveQuestionDialog = None


#search:

	def BINARY_NEW_AddAffect(self, type, pointIdx, value, duration):

#add before

	if app.ENABLE_RENEWAL_AFFECT_SHOWER:
		def CalculatePriority(self, affect):
			# check PRIORITY_FIRST o PRIORITY_LAST
			if affect in PRIORITY_FIRST:
				return 2  # hight priority
			elif affect in PRIORITY_LAST:
				return 5  # low priority

			##changes to organize the list if you use the display system waters, dew and blessings from quin
			priority_ranges = [
				(self.MALL_DESC_IDX_START, self.WATER_DESC_IDX_START, 4),
				# (self.WATER_DESC_IDX_START, self.DEW_DESC_IDX_START, 6),
				# (self.DEW_DESC_IDX_START, self.DEW_DESC_IDX_START + self.DEW_RANGE_OFFSET, 4),
			]

			for start, end, priority in priority_ranges:
				if start <= affect < end:
					return priority

			skillIndex = player.AffectIndexToSkillIndex(affect)
			if skillIndex != 0:
				return 1
			return 3
#search:

	def BINARY_NEW_AddAffect(self, type, pointIdx, value, duration):


#verifies the changes and adds 

	def BINARY_NEW_AddAffect(self, type, pointIdx, value, duration):
		print "BINARY_NEW_AddAffect", type, pointIdx, value, duration
		if app.ENABLE_RENEWAL_AFFECT_SHOWER:
			affect = player.SkillIndexToAffectIndex(type)
			if affect == 0:
				affect = type
			original_affect = affect
			allowed_affects = [
				chr.NEW_AFFECT_POLYMORPH,
			]
			if app.BL_REMOTE_SHOP:
				allowed_affects.append(chr.AFFECT_REMOTE_SHOP)

			Skill_affects = [
				chr.AFFECT_JEONGWI,
				chr.AFFECT_GEOMGYEONG,
				chr.AFFECT_CHEONGEUN,
				chr.AFFECT_FALLEN_CHEONGEUN,
				chr.AFFECT_GYEONGGONG,
				chr.AFFECT_EUNHYEONG,
				chr.AFFECT_GWIGEOM,
				chr.AFFECT_GONGPO,
				chr.AFFECT_JUMAGAP,
				chr.AFFECT_HOSIN,
				chr.AFFECT_BOHO,
				chr.AFFECT_KWAESOK,
				chr.AFFECT_HEUKSIN,
				chr.AFFECT_MUYEONG,
				chr.AFFECT_GICHEON,
				chr.AFFECT_JEUNGRYEOK,
				chr.AFFECT_PABEOP,
			]

			if type < 500 and type not in allowed_affects and affect not in Skill_affects:
				return
		else:
			if type < 500:
				return

		if type == chr.NEW_AFFECT_MALL:
			affect = self.MALL_DESC_IDX_START + pointIdx
		else:
			if app.ENABLE_RENEWAL_AFFECT_SHOWER:
				affect = original_affect
			else:
				affect = type

		if app.ENABLE_RENEWAL_AFFECT_SHOWER:
			if self.affectImageDict.get(affect):
				if player.AffectIndexToSkillIndex(affect) == 0:
					return
		else:
			if self.affectImageDict.get(affect):
				return

		if affect not in self.AFFECT_DATA_DICT:
			return

		if app.ENABLE_RENEWAL_AFFECT_SHOWER:
			priority = self.CalculatePriority(affect)

		if affect in [
			chr.NEW_AFFECT_NO_DEATH_PENALTY,
			chr.NEW_AFFECT_SKILL_BOOK_BONUS,
			chr.NEW_AFFECT_AUTO_SP_RECOVERY,
			chr.NEW_AFFECT_AUTO_HP_RECOVERY,
			chr.NEW_AFFECT_SKILL_BOOK_NO_DELAY,
		]:
			duration = 0

		affectData = self.AFFECT_DATA_DICT[affect]
		description = affectData[0]
		filename = affectData[1]

		if pointIdx == player.POINT_MALL_ITEMBONUS or\
		   pointIdx == player.POINT_MALL_GOLDBONUS:
			value = 1 + float(value) / 100.0

		if affect != chr.NEW_AFFECT_AUTO_SP_RECOVERY and affect != chr.NEW_AFFECT_AUTO_HP_RECOVERY:
			if callable(description):
				description = description(float(value))

		try:
			print "Add affect %s" % affect
			image = AffectImage()
			image.SetParent(self)
			image.LoadImage(filename)
			image.SetDescription(description)
			image.SetDuration(duration)
			image.SetAffect(affect)

			if affect == player.SkillIndexToAffectIndex(type) and app.ENABLE_RENEWAL_AFFECT_SHOWER:
				skillIndex = player.AffectIndexToSkillIndex(player.SkillIndexToAffectIndex(type))
				image.SetSkillIndex(skillIndex)
				image.SetSkillAffectFlag(True)
				image.SetCanberemoved(True)
				image.UpdateSkillDescription()
				image.SetEvent(ui.__mem_func__(self.__QuestionRemoveAffect),"mouse_click", skillIndex, description)
			else:
				image.SetSkillAffectFlag(False)
				EXP_BONUS_AFFECTS = {chr.NEW_AFFECT_EXP_BONUS_EURO_FREE, chr.NEW_AFFECT_EXP_BONUS_EURO_FREE_UNDER_15}
				AUTO_POTION_AFFECTS = {chr.NEW_AFFECT_AUTO_SP_RECOVERY, chr.NEW_AFFECT_AUTO_HP_RECOVERY}
				if affect in EXP_BONUS_AFFECTS or self.INFINITE_AFFECT_DURATION < duration:
					if not app.ENABLE_RENEWAL_AFFECT_SHOWER:
						image.SetClock(False)
					image.UpdateDescription()
				elif affect in AUTO_POTION_AFFECTS:
					image.UpdateAutoPotionDescription()
				elif affect == chr.NEW_AFFECT_POLYMORPH and app.ENABLE_RENEWAL_AFFECT_SHOWER:
					image.UpdateDescription()
					image.SetCanberemoved(True)
					image.SetEvent(ui.__mem_func__(self.__QuestionRemoveAffect),"mouse_click", affect, description)
				else:
					image.UpdateDescription()

			DRAGON_SOUL_AFFECTS = {chr.NEW_AFFECT_DRAGON_SOUL_DECK1, chr.NEW_AFFECT_DRAGON_SOUL_DECK2}
			if affect in DRAGON_SOUL_AFFECTS:
				image.SetScale(1, 1)
			else:
				image.SetScale(0.7, 0.7)

			if app.ENABLE_RENEWAL_AFFECT_SHOWER:
				image.SetPriority(priority)

			image.Show()
			self.affectImageDict[affect] = image
			self.__ArrangeImageList()
		except Exception, e:
			print "except Aff affect ", e
			pass

## Search:
	def __AppendAffect(self, affect):
		[...]
		image.SetSkillAffectFlag(True)

#add
		if app.ENABLE_RENEWAL_AFFECT_SHOWER:
			priority = self.CalculatePriority(affect)
			image.SetPriority(priority)

## Search:
	def __AppendAffect(self, affect):
		[...]
		image.SetToolTipText(name, 0, 40)

## replace with:
	def __AppendAffect(self, affect):
		[...]
		if app.ENABLE_RENEWAL_AFFECT_SHOWER:
			if skillIndex != 0:
				image.SetCanberemoved(True)
				image.SetToolTipText(name)
				image.SetEvent(ui.__mem_func__(self.__QuestionRemoveAffect),"mouse_click", skillIndex, name)
			else:
				image.SetToolTipText(name)
		else:
			image.SetToolTipText(name, 0, 40)


## find:
	def __ArrangeImageList(self):
		[...]

## replace with:

	if app.ENABLE_RENEWAL_AFFECT_SHOWER:
		def __ArrangeImageList(self):
			ordered_elements = sorted(
				self.affectImageDict.values(),
				key=lambda image: image.GetPriority()
			)

			xPos, yPos = 0, 0
			xMax = 0
			countRow = 0

			if self.lovePointImage and self.lovePointImage.IsShow():
				self.lovePointImage.SetPosition(xPos, yPos)
				xPos += self.IMAGE_STEP
				countRow += 1

			if self.horseImage:
				self.horseImage.SetPosition(xPos, yPos)
				xPos += self.IMAGE_STEP
				countRow += 1

			for count, image in enumerate(ordered_elements):
				image.SetPosition(xPos, yPos)
				xPos += self.IMAGE_STEP
				countRow += 1

				if xMax < xPos:
					xMax = xPos

				if countRow == self.MAX_ITEMS_PER_ROW:
					xPos = 0
					yPos += self.IMAGE_STEP
					countRow = 0

			self.SetSize(xMax if xMax > 0 else self.IMAGE_STEP * self.MAX_ITEMS_PER_ROW, yPos + 26)
	else:
		def __ArrangeImageList(self):
			width = len(self.affectImageDict) * self.IMAGE_STEP
			if self.lovePointImage:
				width+=self.IMAGE_STEP
			if self.horseImage:
				width+=self.IMAGE_STEP

			self.SetSize(width, 26)

			xPos = 0

			if self.lovePointImage:
				if self.lovePointImage.IsShow():
					self.lovePointImage.SetPosition(xPos, 0)
					xPos += self.IMAGE_STEP

			if self.horseImage:
				self.horseImage.SetPosition(xPos, 0)
				xPos += self.IMAGE_STEP

			for image in self.affectImageDict.values():
				image.SetPosition(xPos, 0)
				xPos += self.IMAGE_STEP

## Search:
	def OnUpdate(self):
		[...]


## replace with:
	def OnUpdate(self):
		try:
			currentTime = app.GetGlobalTime()
			if currentTime - self.lastUpdateTime > self.TOOLTIP_UPDATE_INTERVAL:
				self.lastUpdateTime = currentTime

				for image in self.affectImageDict.values():
					if not image.isToolTipVisible:
						continue

					if image.GetAffect() in [chr.NEW_AFFECT_AUTO_HP_RECOVERY, chr.NEW_AFFECT_AUTO_SP_RECOVERY]:
						image.UpdateAutoPotionDescription()
					elif image.IsSkillAffect():
						image.UpdateSkillDescription()
					else:
						image.UpdateDescription()
		except Exception as e:
			print "AffectShower::OnUpdate error:", e


# search 

	def OnUpdate(self):

# add:

	if app.ENABLE_RENEWAL_AFFECT_SHOWER:
		def SyncAffectImages(self):
			for image in self.affectImageDict.values():
				image.isToolTipVisible = False
				image.toolTip.HideToolTip()

		def __QuestionRemoveAffect(self, arg, affect, name):
			self.RemoveQuestionDialog = uiCommon.QuestionDialog()
			self.RemoveQuestionDialog.SetText(localeInfo.AFFECT_REMOVE_QUESTION % name)
			self.RemoveQuestionDialog.SetAcceptEvent(lambda arg=True: self.AnswerRemoveAffect(arg))
			self.RemoveQuestionDialog.SetCancelEvent(lambda arg=False: self.AnswerRemoveAffect(arg))
			self.RemoveQuestionDialog.affect = affect
			self.RemoveQuestionDialog.Open()

		def AnswerRemoveAffect(self, flag):
			if not self.RemoveQuestionDialog:
				return
			if flag:
				net.SendChatPacket("/remove_affect %d" % self.RemoveQuestionDialog.affect)
			self.RemoveQuestionDialog.Close()
			self.RemoveQuestionDialog = None





