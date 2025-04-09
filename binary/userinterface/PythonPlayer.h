// Search:
		bool	AffectIndexToSkillIndex(DWORD dwAffectIndex, DWORD * pdwSkillIndex);

// add:
#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
		bool	SkillIndexToAffectIndex(DWORD dwSkillIndex, DWORD * pdwAffectIndex);
#endif

// Search:

		std::map<DWORD, DWORD> m_kMap_dwAffectIndexToSkillIndex;

// Add:

#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
		std::map<DWORD, DWORD> m_kMap_dwSkillIndexToAffectIndex;
#endif
