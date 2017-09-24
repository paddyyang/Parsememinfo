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
import java.util.ArrayList;

//ref code: http://blog.nimbledroid.com/2016/05/23/memory-leaks.html
//save as static view memory leak

public class TestStaticActivity extends  Activity  
{
	private static final String TAG = "MemoryLeakTest";
	EditText edit_text;
    Button button;
    static ArrayList<Activity> activity = new ArrayList();

	@Override
	protected  void  onCreate(Bundle  savedInstanceState)  
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.test_static_activity);
		 
		edit_text = (EditText)findViewById(R.id.edit_text);
		button  =  (Button)findViewById(R.id.button);
		button.setOnClickListener(new  View.OnClickListener()  {
		@Override
		public  void  onClick(View  v)  {
		    setStaticActivity();
            //nextActivity();
            finish();
		}
		});
		
	}

    void setStaticActivity() {

             if(!activity.contains(this)){
                activity.add(this);
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
