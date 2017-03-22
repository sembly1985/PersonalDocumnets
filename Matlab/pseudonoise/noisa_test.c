/******************************************************************************
* @F_NAME :          noisa.c
* @F_PURPOSE :       Purpose
* @F_CREATED_BY :    Shengping Wang
* @F_CREATION_DATE : 2015-08-26
* @F_LANGUAGE :      C
* @F_MPROC_TYPE :   Both endian
*************************************** (C) Copyright 2015 Midea Group   *****/
/*______ I N C L U D E - F I L E S ___________________________________________*/
#include "syst.h"
#include "noisa.h"
/*______ L O C A L - D E F I N E S ___________________________________________*/

/*______ L O C A L - T Y P E S _______________________________________________*/ 

/*______ G L O B A L - D A T A _______________________________________________*/

/*______ P R I V A T E - D A T A _____________________________________________*/

/*______ L O C A L - D A T A _________________________________________________*/
NOISA_PseudoRandNoise_t test;
/*______ L O C A L - M A C R O S _____________________________________________*/

/*______ I M P O R T - F U N C T I O N S - P R O T O T Y P E S _______________*/

/*______ L O C A L - F U N C T I O N S - P R O T O T Y P E S _________________*/

/*______ G L O B A L - F U N C T I O N S _____________________________________*/
void NOISA_Init(void)
{
	NOISA_InitPseudoRandNoise(&test,8,0xff);
}

uint8_t NOISA_Update(void)
{
	return NOISA_UpdatePseudoRandNoise(&test);
}

uint32_t NOISA_GetValue(void)
{
    return test.regValue;
}

/*______ P R I V A T E - F U N C T I O N S ___________________________________*/

/*______ L O C A L - F U N C T I O N S _______________________________________*/

/*______ E N D _____ (noisa.c) ____________________________________________*/
