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
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.content.Context;
import java.util.List;
import android.hardware.SensorManager;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;



public class TestSensor extends  Activity implements SensorEventListener 
{
	private static final String TAG = "MemoryLeakTest";
	EditText edit_text;
    Button button;
	
	@Override
	protected  void  onCreate(Bundle  savedInstanceState)  
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.test_sensor);
		 
		edit_text = (EditText)findViewById(R.id.edit_text);
			
		button  =  (Button)findViewById(R.id.button);
		button.setOnClickListener(new  View.OnClickListener()  {
		@Override
		public  void  onClick(View  v)  {
		    registerListener();
            finish();
		}
		});
	}
    void registerListener() {
           SensorManager sensorManager = (SensorManager) getSystemService(SENSOR_SERVICE);
           Sensor sensor = sensorManager.getDefaultSensor(Sensor.TYPE_ALL);
           sensorManager.registerListener(this, sensor, SensorManager.SENSOR_DELAY_FASTEST);
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

     @Override
     public void onAccuracyChanged(Sensor sensor, int accuracy) {
     
     }

     //传感器数据变动事件
     @Override
     public void onSensorChanged(SensorEvent event) {   
    
     }
}
