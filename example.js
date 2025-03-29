//это пример ответа списка звонков
const a = [
  {
    id: "asdfkjsadf123",
    clientTel: "+7 (999) 999 99 99",
    managerId: "asdfghjjk2423",
    duration: 240,
    avgPauseLen: 7,
    maxPauseLen: 14,
    rating: 30,
    recommendations: [
      "какая-то рекомендация",
      "какая-то другая рекомендация"
    ],
    competition: {
      contact: {
        rating: 40,
        values: {
          clientName: true,
          nameAndCompany: true,
          clientSphere: true,
          lpr: false,
          meeting: true
        }
      },
      effectiveCommunication: {
        rating: 6,
        values: {
          process: false,
          analogs: true,
          issues: true,
          clarifyingQuestions: true,
          openQuestions: true,
          notInterrupt: false,
          activeListening: true,
          summarizeInfo: true
        }
      },
      presentation: {
        rating: 3,
        values: {
          useClientNeeds: true,
          answerClientQuestions: true,
          showBenefit: false,
          showHightPriceFirst: false,
          activeExamples: true
        }
      },
      convincingArguments: {
        rating: 4,
        values: {   
          processClientsObjections: false,
          askClientObjections: true,
          checkClientExtraQuestions: true
        }
      },
      resultOrientation: {
        rating: 9,
        values: {
          useActivePhrase: true,
          recordAgreements: false,
          setNextStep: false,
          offerDeal: true,
          clientNotReadyActions: false,
          buyBuy: false
        }
      },
      initiative: {
        rating: 5,
        values: {
          takesInitiative: true,
          equalsPosition: false
        }
      },
      clientOrientation: {
        rating: 4,
        values: {
          useClientName: false,
        }
      },
      cpm: {
        rating: 4,
        values: {
          actualDeal: false,
          requiredFields: true,
          surnameField: false,
          positivePhrases: true
        }
      },

    }
  }
];

//это пример ответа средних показателей

const b = {
  avg: {
    processedCallRecords: 100,
    avgPauseLen: 10,
    avgMaxPauseLen: 20,
    avgDuration: 30
  },
  days: [   
    {
      date: "2021-01-01",
      hours: [
        {
          hour: 12, // 12:00 - 13:00
          rating: 60,
          competitions: {
            contact: 12,
            effectiveCommunication: 12,
            presentation: 3,
            convincingArguments: 12,
            resultOrientation: 12,
            initiative: 12,
            clientOrientation: 3,
            cpm: 5
          },
          processedCallRecords: 100,
          avgPauseLen: 10,
          avgMaxPauseLen: 20,
          avgDuration: 30
        }
      ]
    }
  ]
}

