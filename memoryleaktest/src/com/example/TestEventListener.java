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
//this sample comes from "Testing of Memory Leak in Android Applications"
public class TestEventListener extends  Activity  
{
	private static final String TAG = "MemoryLeakTest";
    private static int click_number = 0;
	EditText edit_text;
    Button button;
    private byte[] m;
	
	@Override
	protected  void  onCreate(Bundle  savedInstanceState)  
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.test1);
		 
		edit_text = (EditText)findViewById(R.id.edit_text);
			
		button  =  (Button)findViewById(R.id.button);
		button.setOnClickListener(new  View.OnClickListener()  {
		@Override
		public  void  onClick(View  v)  {
			
            m = new byte[1024*1024*10];
            click_number ++;
            Log.e(TAG, "click_number: " + click_number);
            //edit_text.setText(MainActivity.this + " click_number: " + click_number);
            int[] location = new int[2];  
            button.getLocationOnScreen(location);  
            int x = location[0];  
            int y = location[1];  
            Log.e(TAG, "x:"+x+", y:"+y + ", Left："+ button.getLeft()+", Right："+ button.getRight()+", Top："+button.getTop()+", Bottom："+ button.getBottom());  


            finish();
		}
		});
		
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
