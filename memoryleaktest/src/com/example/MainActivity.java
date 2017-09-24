package com.pyzed.memoryleaktest;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

import android.R.string;
import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import android.content.Intent;

public class MainActivity  extends  Activity  implements View.OnClickListener
{
	private static final String TAG = "MemoryLeakTest";
    Button button;
    Button button1;
    Button button2;
    Button button_test_bitmap;
    Button button_static_activity;
    Button button_anony_class;
    Button button_test_sensor;
	
	@Override
	protected  void  onCreate(Bundle  savedInstanceState)  
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		 
		button1  =  (Button)findViewById(R.id.button1);
		button1.setOnClickListener(this);
		button2  =  (Button)findViewById(R.id.button2);
		button2.setOnClickListener(this);
		button_test_bitmap  =  (Button)findViewById(R.id.button_load_bitmap);
		button_test_bitmap.setOnClickListener(this);

		button_static_activity  =  (Button)findViewById(R.id.button_static_activity);
		button_static_activity.setOnClickListener(this);
        //anonymous class leakage
		button_anony_class  =  (Button)findViewById(R.id.button_anony_class);
		button_anony_class.setOnClickListener(this);
        //sensor leakage
		button_test_sensor  =  (Button)findViewById(R.id.button_test_sensor);
		button_test_sensor.setOnClickListener(this);
		
	}

	@Override
    public void onClick(View view) {  
              switch (view.getId()){  
                          case R.id.button1:  
                               Intent intent = new Intent(MainActivity.this, TestEventListener.class);
                               startActivity(intent);
                               break;  
                          case R.id.button2:  
                               intent = new Intent(MainActivity.this, TestLocation.class);
                               startActivity(intent);
                               break;  
                          case R.id.button_load_bitmap:  
                               intent = new Intent(MainActivity.this, TestLoadBitmap.class);
                               startActivity(intent);
                               break;  
                          case R.id.button_static_activity:  
                               intent = new Intent(MainActivity.this, TestStaticActivity.class);
                               startActivity(intent);
                               break;  
                          case R.id.button_anony_class:  
                               intent = new Intent(MainActivity.this, TestAnonyClass.class);
                               startActivity(intent);
                               break;  
                          case R.id.button_test_sensor:  
                               intent = new Intent(MainActivity.this, TestSensor.class);
                               startActivity(intent);
                               break;  
                          default:  
                               break;  
              }  
    }  

	 @Override
	protected void onResume()
	{  	
	    super.onResume();
	}
	 @Override
	protected void onPause()
	{
		super.onPause();
	}
	 @Override
	protected void onDestroy() 
	{
	    super.onDestroy();
	}
}
