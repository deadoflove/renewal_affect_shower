// Search:
bool CPythonPlayer::AffectIndexToSkillIndex(DWORD dwAffectIndex, DWORD * pdwSkillIndex)
{
	if (m_kMap_dwAffectIndexToSkillIndex.end() == m_kMap_dwAffectIndexToSkillIndex.find(dwAffectIndex))
		return false;

	*pdwSkillIndex = m_kMap_dwAffectIndexToSkillIndex[dwAffectIndex];
	return true;
}

// add:
#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
bool CPythonPlayer::SkillIndexToAffectIndex(DWORD dwSkillIndex, DWORD * pdwAffectIndex)
{
	if (m_kMap_dwSkillIndexToAffectIndex.end() == m_kMap_dwSkillIndexToAffectIndex.find(dwSkillIndex))
		return false;

	*pdwAffectIndex = m_kMap_dwSkillIndexToAffectIndex[dwSkillIndex];
	return true;
}
#endif

// Search:

CPythonPlayer::CPythonPlayer(void)

// inside CPythonPlayer::CPythonPlayer(void)

// Search:

	// AffectIndex To SkillIndex
	m_kMap_dwAffectIndexToSkillIndex.emplace(int(CInstanceBase::AFFECT_JEONGWI), 3);
	m_kMap_dwAffectIndexToSkillIndex.emplace(int(CInstanceBase::AFFECT_GEOMGYEONG), 4);
	m_kMap_dwAffectIndexToSkillIndex.emplace(int(CInstanceBase::AFFECT_CHEONGEUN), 19);
	m_kMap_dwAffectIndexToSkillIndex.emplace(int(CInstanceBase::AFFECT_GYEONGGONG), 49);
	m_kMap_dwAffectIndexToSkillIndex.emplace(int(CInstanceBase::AFFECT_EUNHYEONG), 34);
	m_kMap_dwAffectIndexToSkillIndex.emplace(int(CInstanceBase::AFFECT_GONGPO), 64);
	m_kMap_dwAffectIndexToSkillIndex.emplace(int(CInstanceBase::AFFECT_JUMAGAP), 65);
	m_kMap_dwAffectIndexToSkillIndex.emplace(int(CInstanceBase::AFFECT_HOSIN), 94);
	m_kMap_dwAffectIndexToSkillIndex.emplace(int(CInstanceBase::AFFECT_BOHO), 95);
	m_kMap_dwAffectIndexToSkillIndex.emplace(int(CInstanceBase::AFFECT_KWAESOK), 110);
	m_kMap_dwAffectIndexToSkillIndex.emplace(int(CInstanceBase::AFFECT_GICHEON), 96);
	m_kMap_dwAffectIndexToSkillIndex.emplace(int(CInstanceBase::AFFECT_JEUNGRYEOK), 111);
	m_kMap_dwAffectIndexToSkillIndex.emplace(int(CInstanceBase::AFFECT_PABEOP), 66);
	m_kMap_dwAffectIndexToSkillIndex.emplace(int(CInstanceBase::AFFECT_FALLEN_CHEONGEUN), 19);
	/////
	m_kMap_dwAffectIndexToSkillIndex.emplace(int(CInstanceBase::AFFECT_GWIGEOM), 63);
	m_kMap_dwAffectIndexToSkillIndex.emplace(int(CInstanceBase::AFFECT_MUYEONG), 78);
	m_kMap_dwAffectIndexToSkillIndex.emplace(int(CInstanceBase::AFFECT_HEUKSIN), 79);

#ifdef ENABLE_WOLFMAN_CHARACTER
	m_kMap_dwAffectIndexToSkillIndex.emplace(int(CInstanceBase::AFFECT_RED_POSSESSION), 174);
	m_kMap_dwAffectIndexToSkillIndex.emplace(int(CInstanceBase::AFFECT_BLUE_POSSESSION), 175);
#endif


//add:

#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
	// SkillIndex To AffectIndex
	m_kMap_dwSkillIndexToAffectIndex.emplace(3, int(CInstanceBase::AFFECT_JEONGWI));
	m_kMap_dwSkillIndexToAffectIndex.emplace(4, int(CInstanceBase::AFFECT_GEOMGYEONG));
	m_kMap_dwSkillIndexToAffectIndex.emplace(19, int(CInstanceBase::AFFECT_CHEONGEUN));
	m_kMap_dwSkillIndexToAffectIndex.emplace(49, int(CInstanceBase::AFFECT_GYEONGGONG));
	m_kMap_dwSkillIndexToAffectIndex.emplace(34, int(CInstanceBase::AFFECT_EUNHYEONG));
	m_kMap_dwSkillIndexToAffectIndex.emplace(64, int(CInstanceBase::AFFECT_GONGPO));
	m_kMap_dwSkillIndexToAffectIndex.emplace(65, int(CInstanceBase::AFFECT_JUMAGAP));
	m_kMap_dwSkillIndexToAffectIndex.emplace(94, int(CInstanceBase::AFFECT_HOSIN));
	m_kMap_dwSkillIndexToAffectIndex.emplace(95, int(CInstanceBase::AFFECT_BOHO));
	m_kMap_dwSkillIndexToAffectIndex.emplace(110, int(CInstanceBase::AFFECT_KWAESOK));
	m_kMap_dwSkillIndexToAffectIndex.emplace(96, int(CInstanceBase::AFFECT_GICHEON));
	m_kMap_dwSkillIndexToAffectIndex.emplace(111, int(CInstanceBase::AFFECT_JEUNGRYEOK));
	m_kMap_dwSkillIndexToAffectIndex.emplace(66, int(CInstanceBase::AFFECT_PABEOP));
	m_kMap_dwSkillIndexToAffectIndex.emplace(19, int(CInstanceBase::AFFECT_FALLEN_CHEONGEUN));
	m_kMap_dwSkillIndexToAffectIndex.emplace(63, int(CInstanceBase::AFFECT_GWIGEOM));
	m_kMap_dwSkillIndexToAffectIndex.emplace(78, int(CInstanceBase::AFFECT_MUYEONG));
	m_kMap_dwSkillIndexToAffectIndex.emplace(79, int(CInstanceBase::AFFECT_HEUKSIN));

#ifdef ENABLE_WOLFMAN_CHARACTER
	m_kMap_dwSkillIndexToAffectIndex.emplace(174, int(CInstanceBase::AFFECT_RED_POSSESSION));
	m_kMap_dwSkillIndexToAffectIndex.emplace(175, int(CInstanceBase::AFFECT_BLUE_POSSESSION));
#endif

#endif
