// add at the end

#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
ACMD(do_remove_affect)
{
	if (!ch) {
		sys_err("do_remove_affect: The character is not valid.");
		return;
	}

	char arg1[256];
	one_argument(argument, arg1, sizeof(arg1));

	if (!*arg1) {
		ch->ChatPacket(CHAT_TYPE_INFO, "[LS;1980]");
		return;
	}

	DWORD affect = 0;
	str_to_number(affect, arg1);

	constexpr std::array<DWORD, 9> nonRemovableAffects = {
		AFFECT_BLEND,
		AFFECT_MOV_SPEED,
		AFFECT_ATT_SPEED,
		AFFECT_BLOCK_CHAT,
		AFFECT_POISON,
		AFFECT_STUN,
		AFFECT_SLOW,
		AFFECT_FIRE,
		66 // ID additional
	};

	if (std::find(nonRemovableAffects.begin(), nonRemovableAffects.end(), affect) != nonRemovableAffects.end()) {
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("[LS;1979]"));
		return;
	}

	if (AFFECT_POLYMORPH == affect) {
		if (!ch->IsPolymorphed()) {
			return;
		}
		ch->SetPolymorph(0);
	}

	if (ch->FindAffect(affect))
		ch->RemoveAffect(affect);
}
#endif