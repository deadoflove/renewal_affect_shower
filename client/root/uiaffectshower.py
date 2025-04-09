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

# within the class AutoPotionImage search

	def OnMouseOverIn(self):
		self.toolTip.ShowToolTip()

# add:

		if app.ENABLE_RENEWAL_AFFECT_SHOWER:
			self.SetScale(0.9,0.9)

# Search:

class AutoPotionImage(ui.ExpandedImageBox):

# within the class AutoPotionImage search

	def OnMouseOverOut(self):
		self.toolTip.HideToolTip()

# add:

		if app.ENABLE_RENEWAL_AFFECT_SHOWER:
			self.SetScale(0.7, 0.7)


# check this class carefully

class AffectImage(ui.ExpandedImageBox):

# modify it, it is added all the defines in every change

class AffectImage(ui.ExpandedImageBox):

	def __init__(self):
		ui.ExpandedImageBox.__init__(self)

		if app.ENABLE_RENEWAL_AFFECT_SHOWER:
			self.toolTip = uiToolTip.ToolTip()
			self.toolTip.HideToolTip()
		else:
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

	if app.ENABLE_RENEWAL_AFFECT_SHOWER:
		def FormatTime(self, time):
			text = ""

			d = time // (24 * 3600)
			time = time % (24 * 3600)
			h = time // 3600
			time %= 3600
			m = time // 60
			time %= 60
			s = time

			if d:
				text += "%dd " % d
			if text or h:
				text += "%dh " % h
			if text or m:
				text += "%dm " % m
			if text or s:
				text += "%ds " % s

			return text[:-1]

		def SetToolTipText(self, text, x = 0, y = -19):
			self.toolTip.ClearToolTip()
			self.toolTip.AppendSpace(-5)
			self.toolTip.AppendDescription(text, 26)
	else:
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
		if app.ENABLE_RENEWAL_AFFECT_SHOWER:
			self.__UpdateDescription2()

	def SetDuration(self, duration):
		self.endTime = 0
		if duration > 0:
			self.endTime = app.GetGlobalTimeStamp() + duration
			if app.ENABLE_RENEWAL_AFFECT_SHOWER:
				leftTime = self.FormatTime(self.endTime - app.GetGlobalTimeStamp())
				self.toolTip.AppendTextLine("(%s : %s)" % (localeInfo.LEFT_TIME, leftTime), 0xffC5C7C4)
				self.toolTip.ResizeToolTip()

	if app.ENABLE_RENEWAL_AFFECT_SHOWER:
		def UpdateSkillDescription(self, skillIndex):
			slotIndex = player.GetSkillSlotIndex(skillIndex)
			skillCurrentPercentage = player.GetSkillCurrentEfficientPercentage(slotIndex)
			if self.toolTip:
				self.toolTip.ClearToolTip()

			skillName = skill.GetSkillName(skillIndex)
			self.toolTip.AppendTextLine(skillName, 0xffffffff)

			for i in xrange(skill.GetSkillAffectDescriptionCount(skillIndex)):
				description = skill.GetSkillAffectDescription(skillIndex, i, skillCurrentPercentage)
				self.toolTip.AppendTextLine(description, 0xff95A693)

			self.toolTip.ResizeToolTip()

	def UpdateAutoPotionDescription(self):
		potionType = 0
		if self.affect == chr.NEW_AFFECT_AUTO_HP_RECOVERY:
			potionType = player.AUTO_POTION_TYPE_HP
		else:
			potionType = player.AUTO_POTION_TYPE_SP

		isActivated, currentAmount, totalAmount, slotIndex = player.GetAutoPotionInfo(potionType)
		amountPercent = 0.0
		try:
			amountPercent = (float(currentAmount) / totalAmount) * 100.0
		except:
			amountPercent = 100.0

		if app.ENABLE_RENEWAL_AFFECT_SHOWER:
			self.toolTip.childrenList[-1].SetText(self.description % amountPercent)
		else:
			self.SetToolTipText(self.description % amountPercent, 0, 40)

	def SetClock(self, isClocked):
		self.isClocked = isClocked
		if app.ENABLE_RENEWAL_AFFECT_SHOWER:
			self.SetDescription(self.description)

	def UpdateDescription(self):
		if not self.isClocked:
			self.__UpdateDescription2()
			return

		if not self.description:
			return

		if app.ENABLE_RENEWAL_AFFECT_SHOWER:
			if self.endTime > 0:
				leftTime = self.FormatTime(self.endTime - app.GetGlobalTimeStamp())
				timeText = "(%s : %s)" % (localeInfo.LEFT_TIME, leftTime)
				timeLine = None
				for line in self.toolTip.childrenList:
					if "(%s :" % localeInfo.LEFT_TIME in line.GetText():
						timeLine = line
						break

				if timeLine:
					timeLine.SetText(timeText)
					timeLine.SetPackedFontColor(0xffC5C7C4)
				else:
					self.toolTip.AppendTextLine(timeText, 0xffC5C7C4)
			self.toolTip.ResizeToolTip()
		else:
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
		if app.ENABLE_RENEWAL_AFFECT_SHOWER:
			self.SetScale(0.9,0.9)
			self.toolTip.ShowToolTip()
		else:
			if self.toolTipText:
				self.toolTipText.Show()

	def OnMouseOverOut(self):
		if app.ENABLE_RENEWAL_AFFECT_SHOWER:
			self.SetScale(0.7, 0.7)
			self.toolTip.HideToolTip()
		else:
			if self.toolTipText:
				self.toolTipText.Hide()


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

#search:

	def BINARY_NEW_AddAffect(self, type, pointIdx, value, duration):
		print "BINARY_NEW_AddAffect", type, pointIdx, value, duration

		if type < 500:
			return

# replace

	def BINARY_NEW_AddAffect(self, type, pointIdx, value, duration):
		print "BINARY_NEW_AddAffect", type, pointIdx, value, duration

		if app.ENABLE_RENEWAL_AFFECT_SHOWER:
			SkillIndexToAffect = player.SkillIndexToAffectIndex(type)
			AffectToskillIndex = player.AffectIndexToSkillIndex(SkillIndexToAffect)

			#here you can add new effects that do not require you to define them, 
			#for example the polymorph and if you want to add the blend
			allowed_affects = [
				chr.NEW_AFFECT_POLYMORPH,
			]
			#note in this way you can add new affect to show that you have defined, 
			# for example I created an affect to load by time the opening of the remote shop.
			# if app.BL_REMOTE_SHOP:
				# allowed_affects.append(chr.AFFECT_REMOTE_SHOP)

			if type < 500 and type not in allowed_affects and not type == AffectToskillIndex:
				return
		else:
			if type < 500:
				return

# Search:

		if not self.AFFECT_DATA_DICT.has_key(affect):
			return

#replace:

		if app.ENABLE_RENEWAL_AFFECT_SHOWER:
			if affect not in self.AFFECT_DATA_DICT:
				converted_affect = player.SkillIndexToAffectIndex(affect)
				if converted_affect in self.AFFECT_DATA_DICT:
					affect = converted_affect
				else:
					# If unable to convert, stop the flow
					# chat.AppendChat(chat.CHAT_TYPE_INFO, "Affect not found for skillIndex: " + str(affect))
					return
		else:
			if not self.AFFECT_DATA_DICT.has_key(affect):
				return

#search:

			elif affect == chr.NEW_AFFECT_AUTO_SP_RECOVERY or affect == chr.NEW_AFFECT_AUTO_HP_RECOVERY:
				image.UpdateAutoPotionDescription()

#add:

			elif affect == SkillIndexToAffect and app.ENABLE_RENEWAL_AFFECT_SHOWER:
				skillIndex = player.AffectIndexToSkillIndex(SkillIndexToAffect)
				image.UpdateSkillDescription(skillIndex)

## Search:
	def BINARY_NEW_AddAffect(self, type, pointIdx, value, duration):
		[...]
			self.__ArrangeImageList()

## replace with:
	def BINARY_NEW_AddAffect(self, type, pointIdx, value, duration):
		[...]
			if not app.ENABLE_RENEWAL_AFFECT_SHOWER:
				self.__ArrangeImageList()

## find:
	def BINARY_NEW_RemoveAffect(self, type, pointIdx):
		[...]
		self.__ArrangeImageList()

## replace with:
	def BINARY_NEW_RemoveAffect(self, type, pointIdx):
		[...]
		if not app.ENABLE_RENEWAL_AFFECT_SHOWER:
			self.__ArrangeImageList()

## paste below:
	if app.ENABLE_RENEWAL_AFFECT_SHOWER:
		def BINARY_NEW_RefreshAffect(self):
			self.__ArrangeImageList()


## find:
	def __ArrangeImageList(self):
		[...]

## replace with:

	if app.ENABLE_RENEWAL_AFFECT_SHOWER:
		def __ArrangeImageList(self):
			xPos = 0
			yPos = 0

			xMax = 0

			countRow = 0

			if self.lovePointImage:
				if self.lovePointImage.IsShow():
					self.lovePointImage.SetPosition(xPos, yPos)
					xPos += self.IMAGE_STEP
					countRow += 1

			if self.horseImage:
				self.horseImage.SetPosition(xPos, yPos)
				xPos += self.IMAGE_STEP
				countRow += 1

			for image in self.affectImageDict.values():
				image.SetPosition(xPos, yPos)
				xPos += self.IMAGE_STEP
				countRow += 1

				if xMax < xPos:
					xMax = xPos

				if countRow == 10:
					xPos = 0
					yPos += self.IMAGE_STEP
					countRow = 0

			self.SetSize(xMax, yPos + 26)
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
