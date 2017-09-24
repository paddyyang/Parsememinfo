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



public class TestLocation extends  Activity  
{
	private static final String TAG = "MemoryLeakTest";
	EditText edit_text;
    Button button;
    private LocationManager mLocationManager = null;
	
	@Override
	protected  void  onCreate(Bundle  savedInstanceState)  
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.test_location);
		 
		edit_text = (EditText)findViewById(R.id.edit_text);
			
		button  =  (Button)findViewById(R.id.button);
		button.setOnClickListener(new  View.OnClickListener()  {
		@Override
		public  void  onClick(View  v)  {
			
		}
		});


        LocationManager lm = (LocationManager)getSystemService(Context.LOCATION_SERVICE);

        if(lm.isProviderEnabled(LocationManager.GPS_PROVIDER)){
                //locationManager.requestLocationUpdates(LocationManager.NETWORK_PROVIDER, 0, 0, locationListener);
                lm.requestLocationUpdates(LocationManager.GPS_PROVIDER, 0, 0, new LocationListener() {
                        @Override
                        public void onStatusChanged(String provider, int status, Bundle extras) {}

                        @Override
                        public void onProviderEnabled(String provider) {}

                        @Override
                        public void onProviderDisabled(String provider) {}

                        @Override
                        public void onLocationChanged(Location location) {
                               if (location != null) {
                                   Log.d(TAG, "onLocationChanged: " + location);
                               }
                        }
                });
        } else {
            Log.d(TAG, "can not use LocationManager.NETWORK_PROVIDER!");
        }

        List<String> allproviders=lm.getAllProviders();
        for(String allprovide:allproviders){
            Log.d(TAG, "All providers: " + allproviders);
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
