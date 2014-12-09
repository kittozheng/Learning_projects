@extends('admin._layouts.default')
 
@section('main')
 
    <h2>Page Content</h2>

        <div id="onepage">
            
            <div class="title">
                <h3>{{ $page->title }}</h3>
            </div>

            <div class="info">
                {{ $author }} pulished at {{ $page->created_at }}  and last updated {{ $page->updated_at }}
            </div>

            <div class="body">
                {{ $page->body }}
            </div>

        </div>
 
@stop