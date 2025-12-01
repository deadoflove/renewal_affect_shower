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



// If you use any system to hide or show the affects, you can use this.

// search
		void	ClearAffects();
// add
#if defined(ENABLE_RENEWAL_AFFECT_SHOWER)
		void	ShowAffectShower();
		void	HideAffectShower();
#endif