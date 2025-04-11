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


# update, set your old class to else:

class AffectImage(ui.ExpandedImageBox):

# replace

if app.ENABLE_RENEWAL_AFFECT_SHOWER:
	class AffectImage(ui.ExpandedImageBox):
		def __init__(self):
			ui.ExpandedImageBox.__init__(self)

			self.toolTip = uiToolTip.ToolTip()
			self.toolTip.HideToolTip()
			self.isToolTipVisible = False  # The tooltip is not initially visible
			self.skillIndex = None  # New attribute to store the skill index
			self.isSkillAffect = True
			self.description = None
			self.endTime = 0
			self.affect = None

		def SetAffect(self, affect):
			self.affect = affect

		def GetAffect(self):
			return self.affect

		def SetToolTipText(self, text):
			# Check if the text is already configured
			if hasattr(self, "currentToolTipText") and self.currentToolTipText == text:
				return  # Do nothing if text is already configured

			self.toolTip.ClearToolTip()
			self.toolTip.AppendTextLine(text, 0xffffffff)
			self.toolTip.AlignHorizonalCenter()
			self.toolTip.ResizeToolTip()
			# Store current text
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
			else:
				potionType = player.AUTO_POTION_TYPE_SP

			isActivated, currentAmount, totalAmount, slotIndex = player.GetAutoPotionInfo(potionType)

			amountPercent = 0.0

			try:
				amountPercent = (float(currentAmount) / totalAmount) * 100.0
			except:
				amountPercent = 100.0

			# Clean the tooltip before upgrading
			self.toolTip.ClearToolTip()

			# Add the description of the automatic potion
			self.toolTip.AppendTextLine(self.description % amountPercent, 0xffC5C7C4)

			# Resize the tooltip
			self.toolTip.ResizeToolTip()

		def FormatTime(self, time):
			if time < 0:
				return "0s"  # Be sure to manage negative times

			(d, remainder) = divmod(time, 86400)
			(h, remainder) = divmod(remainder, 3600)
			(m, s) = divmod(remainder, 60)

			# Create a list of non-empty values
			time_parts = [
				"{}d".format(d) if d > 0 else "",
				"{}h".format(h) if h > 0 else "",
				"{}m".format(m) if m > 0 else "",
				"{}s".format(s) if s > 0 else "",
			]

			# Filter out empty values and join them with a space
			formatted_time = " ".join(filter(None, time_parts))
			return formatted_time

		def UpdateDescription(self):
			# Verify that the tooltip is initialized
			if not self.toolTip:
				return

			# Verify that the description is configured
			if not self.description:
				return

			# Clean the tooltip before upgrading
			self.toolTip.ClearToolTip()

			# Add the main description
			self.toolTip.AppendTextLine(self.description, 0xffC5C7C4)

			# Add remaining time if necessary
			if self.endTime > 0:
				remaining_time = self.endTime - app.GetGlobalTimeStamp()
				leftTime = self.FormatTime(remaining_time)
				timeText = "(%s : %s)" % (localeInfo.LEFT_TIME, leftTime)
				self.toolTip.AppendTextLine(timeText, 0xffC5C7C4)

			# Resize the tooltip
			self.toolTip.ResizeToolTip()

		def SetSkillIndex(self, skillIndex):
			"""Sets the skill index for this instance."""
			self.skillIndex = skillIndex

		def UpdateSkillDescription(self):
			"""Updates the skill description using the stored index."""
			if self.skillIndex is None:
				return  # If there is no skill index, do nothing.

			slotIndex = player.GetSkillSlotIndex(self.skillIndex)
			skillCurrentPercentage = player.GetSkillCurrentEfficientPercentage(slotIndex)

			# Clean the tooltip before upgrading
			self.toolTip.ClearToolTip()

			# Add the name of the skill
			skillName = skill.GetSkillName(self.skillIndex)
			self.toolTip.AppendTextLine(skillName, 0xffffffff)

			# Add skill descriptions
			for i in xrange(skill.GetSkillAffectDescriptionCount(self.skillIndex)):
				description = skill.GetSkillAffectDescription(self.skillIndex, i, skillCurrentPercentage)
				self.toolTip.AppendTextLine(description, 0xff95A693)

			# Add remaining time if necessary
			if self.endTime > 0:
				remaining_time = self.endTime - app.GetGlobalTimeStamp()
				leftTime = self.FormatTime(remaining_time)
				timeText = "(%s : %s)" % (localeInfo.LEFT_TIME, leftTime)
				self.toolTip.AppendTextLine(timeText, 0xffC5C7C4)

			# Resize the tooltip
			self.toolTip.ResizeToolTip()

		def SetSkillAffectFlag(self, flag):
			self.isSkillAffect = flag

		def IsSkillAffect(self):
			return self.isSkillAffect

		def OnMouseOverIn(self):
			self.SetScale(0.9,0.9)
			if self.toolTip:
				self.toolTip.ShowToolTip()
				self.isToolTipVisible = True  # Mark the tooltip as visible

		def OnMouseOverOut(self):
			self.SetScale(0.7,0.7)
			if self.toolTip:
				self.toolTip.HideToolTip()
				self.isToolTipVisible = False  # Mark the tooltip as not visible
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

			if affect == chr.NEW_AFFECT_EXP_BONUS_EURO_FREE or\
				affect == chr.NEW_AFFECT_EXP_BONUS_EURO_FREE_UNDER_15 or\
				self.INFINITE_AFFECT_DURATION < duration:
				image.SetClock(False)
				image.UpdateDescription()
			elif affect == chr.NEW_AFFECT_AUTO_SP_RECOVERY or affect == chr.NEW_AFFECT_AUTO_HP_RECOVERY:
				image.UpdateAutoPotionDescription()
			else:
				image.UpdateDescription()

#replace:

			if affect == SkillIndexToAffect and app.ENABLE_RENEWAL_AFFECT_SHOWER:
				skillIndex = player.AffectIndexToSkillIndex(SkillIndexToAffect)
				image.SetSkillIndex(skillIndex)
				image.SetSkillAffectFlag(True)  # Activate the flag for skills
				image.UpdateSkillDescription()
			else:
				image.SetSkillAffectFlag(False)  # Deactivate the flag for other affects
				if affect == chr.NEW_AFFECT_EXP_BONUS_EURO_FREE or\
					affect == chr.NEW_AFFECT_EXP_BONUS_EURO_FREE_UNDER_15 or\
					self.INFINITE_AFFECT_DURATION < duration:
					if not app.ENABLE_RENEWAL_AFFECT_SHOWER:
						image.SetClock(False)
					image.UpdateDescription()
				elif affect == chr.NEW_AFFECT_AUTO_SP_RECOVERY or affect == chr.NEW_AFFECT_AUTO_HP_RECOVERY:
					image.UpdateAutoPotionDescription()
				else:
					image.UpdateDescription()

## Search:
	def BINARY_NEW_AddAffect(self, type, pointIdx, value, duration):
		[...]
			image.SetSkillAffectFlag(False)

## replace with:
	def BINARY_NEW_AddAffect(self, type, pointIdx, value, duration):
		[...]
			if not app.ENABLE_RENEWAL_AFFECT_SHOWER:
				image.SetSkillAffectFlag(False)

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

## Search:
	def __AppendAffect(self, affect):
		[...]
		image.SetToolTipText(name, 0, 40)

## replace with:
	def __AppendAffect(self, affect):
		[...]
		if app.ENABLE_RENEWAL_AFFECT_SHOWER:
			if skillIndex != 0:
				image.UpdateSkillDescription()
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

## Search:
	def OnUpdate(self):
		[...]
				for image in self.affectImageDict.values():
					if image.GetAffect() == chr.NEW_AFFECT_AUTO_HP_RECOVERY or image.GetAffect() == chr.NEW_AFFECT_AUTO_SP_RECOVERY:
						image.UpdateAutoPotionDescription()
						continue

					if not image.IsSkillAffect():
						image.UpdateDescription()

## replace with:
	def OnUpdate(self):
		[...]
				if app.ENABLE_RENEWAL_AFFECT_SHOWER:
					if image.isToolTipVisible:
						if image.GetAffect() in [chr.NEW_AFFECT_AUTO_HP_RECOVERY, chr.NEW_AFFECT_AUTO_SP_RECOVERY]:
							image.UpdateAutoPotionDescription()
							continue

						if image.IsSkillAffect():
							image.UpdateSkillDescription()
							continue

						if not image.IsSkillAffect():
							image.UpdateDescription()
				else:
					if image.GetAffect() == chr.NEW_AFFECT_AUTO_HP_RECOVERY or image.GetAffect() == chr.NEW_AFFECT_AUTO_SP_RECOVERY:
						image.UpdateAutoPotionDescription()
						continue

					if not image.IsSkillAffect():
						image.UpdateDescription()


# search 

	def OnUpdate(self):

# add:

	if app.ENABLE_RENEWAL_AFFECT_SHOWER:
		def SyncAffectImages(self):
			for image in self.affectImageDict.values():
				image.isToolTipVisible = False  # Reset tooltip status
				image.toolTip.HideToolTip()  # Ensure that the tooltip is initially hidden.


# Search:

	def __init__(self):
		ui.Window.__init__(self)

# add before

	if app.ENABLE_RENEWAL_AFFECT_SHOWER:
		def Show(self):
			ui.Window.Show(self)
			self.SyncAffectImages()