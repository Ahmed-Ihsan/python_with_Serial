#define REMOTEXY_MODE__SOFTSERIAL
#include <SoftwareSerial.h>

#include <RemoteXY.h>

// RemoteXY connection settings 
#define REMOTEXY_SERIAL_RX 2
#define REMOTEXY_SERIAL_TX 3
#define REMOTEXY_SERIAL_SPEED 9600


// RemoteXY configurate  
#pragma pack(push, 1)
uint8_t RemoteXY_CONF[] =   // 102 bytes
  { 255,13,0,0,0,95,0,16,24,1,7,36,0,0,63,9,16,16,136,11,
  129,0,5,33,5,6,137,50,46,32,83,117,104,97,105,98,32,77,117,107,
  100,97,100,0,129,0,5,23,6,5,233,49,46,32,32,73,98,114,97,104,
  101,101,109,32,84,104,97,105,114,0,129,0,5,44,5,6,94,51,46,32,
  83,101,100,105,107,32,83,117,104,97,105,98,0,5,0,15,65,30,30,2,
  26,31 };
  
// this structure defines all the variables and events of your control interface 
struct {

    // input variables
  char edit_1[11];  // string UTF8 end zero  
  int8_t joystick_1_x; // from -100 to 100  
  int8_t joystick_1_y; // from -100 to 100  

    // other variable
  uint8_t connect_flag;  // =1 if wire connected, else =0 

} RemoteXY;
#pragma pack(pop)

/////////////////////////////////////////////
//           END RemoteXY include          //
/////////////////////////////////////////////



void setup() 
{
  RemoteXY_Init (); 
  
  
  Serial.begin(9600);
  
}

void loop() 
{ 
  RemoteXY_Handler ();
  
  
   if ( (strcmp (RemoteXY.edit_1, "ibraheem")==0) || (strcmp (RemoteXY.edit_1, "1")==0) ) {
      Serial.println(RemoteXY.edit_1);
      RemoteXY.edit_1[1] = '-';
    }


    if ( (strcmp (RemoteXY.edit_1, "suhaib")==0) || (strcmp (RemoteXY.edit_1, "2")==0) ) {
      Serial.println(RemoteXY.edit_1);
      RemoteXY.edit_1[1] = '-';
    }


    if ( (strcmp (RemoteXY.edit_1, "sedik")==0) || (strcmp (RemoteXY.edit_1, "3")==0) ) {
      Serial.println(RemoteXY.edit_1);
      RemoteXY.edit_1[1] = '-';
    }



}