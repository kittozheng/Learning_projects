@extends('admin._layouts.default')

@section('main')
	
	<h2> Update Article</h2>

	{{ Notification::showAll() }}

	@if($errors->any())
		<div class="alert alert-error">
			{{ implode('<br>', $errors->all()) }}
		</div>
	@endif

	{{ Form::model($article, array('method'=>'put', 'route'=>array('admin.articles.update', $article->id))) }}
		<div class="control-group">
			{{ Form::label('title', 'Title') }}
			<div class="controls">
				{{ Form::text('title') }}
			</div>		
		</div>

		<div class="control-group">
			{{ Form::label('image', 'Image') }}
			<div class="controls">
				{{ Form::text('image') }}
			</div>		
		</div>

		<div class="control-group'">
			{{ Form::label('body', 'content') }}
			<div class="controls'">
				{{ Form::textarea('body') }}
			</div>
		</div>

		<div class="form-actions">
			{{ Form::submit('Update', array('class'=>'btn btn-success btn-save btn-large')) }}
			<a href="{{ URL::route('admin.articles.index') }}" class="btn btn-large">Cancle</a>
		</div>

	{{ Form::close() }}
@stop