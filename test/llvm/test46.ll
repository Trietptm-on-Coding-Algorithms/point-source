; ModuleID = '../src/test46.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test46() #0 {
  %local1 = alloca i32, align 4
  %local2 = alloca i32, align 4
  %n = alloca i32, align 4
  %m = alloca i32, align 4
  store i32 0, i32* %n, align 4
  br label %1

; <label>:1                                       ; preds = %13, %0
  %2 = load i32* %n, align 4
  %3 = icmp slt i32 %2, 10
  br i1 %3, label %4, label %16

; <label>:4                                       ; preds = %1
  %5 = load i32* %local2, align 4
  %6 = add nsw i32 %5, 10
  store i32 %6, i32* %local2, align 4
  %7 = load i32* %local2, align 4
  %8 = icmp sgt i32 %7, 20
  br i1 %8, label %9, label %12

; <label>:9                                       ; preds = %4
  %10 = load i32* %local1, align 4
  %11 = add nsw i32 %10, 5
  store i32 %11, i32* %local1, align 4
  br label %12

; <label>:12                                      ; preds = %9, %4
  br label %13

; <label>:13                                      ; preds = %12
  %14 = load i32* %n, align 4
  %15 = add nsw i32 %14, 1
  store i32 %15, i32* %n, align 4
  br label %1

; <label>:16                                      ; preds = %1
  %17 = load i32* %local1, align 4
  %18 = load i32* %local2, align 4
  %19 = add nsw i32 %17, %18
  ret i32 %19
}

attributes #0 = { nounwind "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-realign-stack" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"Ubuntu clang version 3.6.2-1 (tags/RELEASE_362/final) (based on LLVM 3.6.2)"}
