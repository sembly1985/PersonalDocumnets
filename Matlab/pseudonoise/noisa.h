/******************************************************************************
* @F_NAME :          noisa.h
* @F_PURPOSE :       Purpose
* @F_CREATED_BY :    Shengping Wang
* @F_CREATION_DATE : 2015-08-26
* @F_LANGUAGE :      C
* @F_MPROC_TYPE :   Both endian
*************************************** (C) Copyright 2015 Midea Group   *****/

#ifndef NOISA_H
#define NOISA_H

/*______ I N C L U D E - F I L E S ___________________________________________*/
#include "syst.h"

/*______ G L O B A L - D E F I N E S _________________________________________*/

/*______ G L O B A L - T Y P E S _____________________________________________*/
typedef struct{
	uint8_t regLen;
	uint32_t regValue;
}NOISA_PseudoRandNoise_t;
/*______ G L O B A L - D A T A _______________________________________________*/

/*______ G L O B A L - M A C R O S ___________________________________________*/

/*______ G L O B A L - F U N C T I O N S - P R O T O T Y P E S _______________*/
extern void NOISA_InitPseudoRandNoise(NOISA_PseudoRandNoise_t *noise, uint8_t len, uint32_t value);
extern uint8_t NOISA_UpdatePseudoRandNoise(NOISA_PseudoRandNoise_t *noise);

extern void NOISA_Init(void);
extern uint8_t NOISA_Update(void);
extern uint32_t NOISA_GetValue(void);
#endif /* NOISA_H */

/* _____ E N D _____ (noisa.h) ____________________________________________*/
